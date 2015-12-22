function makeCheckList() {
    if( document.createElement('svg').getAttributeNS ) {

        var checkbxsList = Array.prototype.slice.call( document.querySelectorAll( 'form.ac-list input[type="checkbox"]' ) ),
            pathDefs = {
                list : ['M1.986,8.91c41.704,4.081,83.952,5.822,125.737,2.867 c17.086-1.208,34.157-0.601,51.257-0.778c21.354-0.223,42.706-1.024,64.056-1.33c18.188-0.261,36.436,0.571,54.609,0.571','M3.954,25.923c9.888,0.045,19.725-0.905,29.602-1.432 c16.87-0.897,33.825-0.171,50.658-2.273c14.924-1.866,29.906-1.407,44.874-1.936c19.9-0.705,39.692-0.887,59.586,0.45 c35.896,2.407,71.665-1.062,107.539-1.188']
            },
            animDefs = {
                list : { speed : .3, easing : 'ease-in-out' }
            };

        function createSVGEl( def ) {
            var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            if( def ) {
                svg.setAttributeNS( null, 'viewBox', def.viewBox );
                svg.setAttributeNS( null, 'preserveAspectRatio', def.preserveAspectRatio );
            }
            else {
                svg.setAttributeNS( null, 'viewBox', '0 0 100 100' );
            }
            svg.setAttribute( 'xmlns', 'http://www.w3.org/2000/svg' );
            return svg;
        }

        function controlCheckbox( el, type, svgDef ) {
            var svg = createSVGEl( svgDef );
            el.parentNode.appendChild( svg );

            el.addEventListener( 'change', function() {
                if( el.checked ) {
                    draw( el, type );
                }
                else {
                    reset( el );
                }
            } );
        }

        checkbxsList.forEach( function( el ) { controlCheckbox( el, 'list', { viewBox : '0 0 300 100', preserveAspectRatio : 'none' } ); } );

        function draw( el, type ) {
            var paths = [], pathDef, 
                animDef,
                svg = el.parentNode.querySelector( 'svg' );

            pathDef = pathDefs.list; animDef = animDefs.list;

            paths.push( document.createElementNS('http://www.w3.org/2000/svg', 'path' ) );

            paths.push( document.createElementNS('http://www.w3.org/2000/svg', 'path' ) );

            console.log('path');

            for( var i = 0, len = paths.length; i < len; ++i ) {
                console.log('path');
                var path = paths[i];
                svg.appendChild( path );

                path.setAttributeNS( null, 'd', pathDef[i] );

                var length = path.getTotalLength();
                // Clear any previous transition
                //path.style.transition = path.style.WebkitTransition = path.style.MozTransition = 'none';
                // Set up the starting positions
                path.style.strokeDasharray = length + ' ' + length;
                if( i === 0 ) {
                    path.style.strokeDashoffset = Math.floor( length ) - 1;
                }
                else path.style.strokeDashoffset = length;
                // Trigger a layout so styles are calculated & the browser
                // picks up the starting position before animating
                path.getBoundingClientRect();
                // Define our transition
                path.style.transition = path.style.WebkitTransition = path.style.MozTransition  = 'stroke-dashoffset ' + animDef.speed + 's ' + animDef.easing + ' ' + i * animDef.speed + 's';
                // Go!
                path.style.strokeDashoffset = '0';
            }
        }

        function reset( el ) {
            Array.prototype.slice.call( el.parentNode.querySelectorAll( 'svg > path' ) ).forEach( function( el ) { el.parentNode.removeChild( el ); } );
        }

    }
}