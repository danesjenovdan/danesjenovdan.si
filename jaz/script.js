if ((window.location.search.indexOf('?') === -1) && (window.location.search.indexOf('&') === -1)) {
    alert('Prosim ne goljufaj. ;)');
    document.location.href = 'https://danesjenovdan.si/';
} else {
    var searchparams = window.location.search
    .split('?')[1]
    .split('&')
    .map(function(val) {
        return {
            'name': val.split('=')[0],
            'value': val.split('=')[1],
        }
    });

    var paramObject = {};
    searchparams.forEach(function(item) {
        paramObject[item.name] = item.value;
    });
}

$(document).ready(function() {
    // if (document.location.href.indexOf('token') === -1) {
    //     $('.logged-out').css('display', 'block');
    //     $('.logged-in').css('display', 'none');
    // }

    $('#person').text(paramObject.email);

    $.get('https://spam.djnd.si/get-settings/?token=' + paramObject.token + '&email=' + paramObject.email, function(r) {
        if (r === 'Ne goljufaj prosim.') {
            alert('Ne goljufaj prosim. ;)');
            document.location.href = 'https://danesjenovdan.si/'
        }
        $('#checkbox-agrument')[0].checked = r.agrument;
        $('#checkbox-djnd')[0].checked = r.djnd;
        $('#checkbox-parlameter')[0].checked = r.parlameter;
        $('#checkbox-konsenz')[0].checked = r.konsenz;
        $('#konsenzname').val(r.name);

        $('.switch').each(function () {
            var label = $(this).parent().parent().find('.toggle-label');
            var checked = $(this).find('input')[0].checked;
            if ($(this).hasClass('switch-konsenz')) {
                label.text(checked ? 'Podpisano!' : 'Podpišite me!');
            } else {
                label.text(checked ? 'Naročeno!' : 'Naročite me!');
            }
        });
    });

    $('.switch input[type="checkbox"]').not('#checkbox-konsenz').on('change', function() {
        var target = $(this).parent().data('target');
        var label = $(this).parent().parent().parent().find('.toggle-label');

        if (this.checked) {
            window.currentConfettis = 0;
            startConfetti();
        }

        // call API here
        url = 'https://spam.djnd.si/confirm-' + target + '/?token=' + paramObject.token + '&email=' + paramObject.email + '&permission=' + this.checked;
        console.log(url);
        $.get(url, function(r) {
            console.log(r);
            if (r !== '1') {
                alert(r);
            } else {
                label.text(this.checked ? 'Naročeno!' : 'Naročite me!');
            }
        });
    });

    $('.switch-konsenz').on('click', function(event) {
        if ($('#konsenzname').val() === '') {
            alert('Da te lahko podpišemo, nam moraš povedati kako ti je ime.')
            event.preventDefault();
        } else if (event.target.tagName === 'INPUT') { // prevent triggering click multiple times
            var target = 'konsenz';
            var checked = $(this).children('input')[0].checked;
            var label = $(this).parent().parent().find('.toggle-label');

            if (checked) {
                window.currentConfettis = 0;
                startConfetti();
            }

            // call API here
            url = 'https://spam.djnd.si/confirm-' + target + '/?token=' + paramObject.token + '&email=' + paramObject.email + '&name=' + $('#konsenzname').val() + '&permission=' + checked;
            console.log(url);
            $.get(url, function(r) {
                console.log(r);
                if (r !== '1') {
                    alert(r);
                } else {
                    label.text(checked ? 'Podpisano!' : 'Podpišite me!');
                }
            });
        }
    });
});
