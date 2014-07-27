var enkratnaHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/donacija.png);" data-img="../../img/donacija.png"></div>',
					'<p class="pregleditemdescription"> Enkratna donacija</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x {{ itemprice }} €</p>',
					'</div>'].join('\n');
var rednaHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/donacija.png);" data-img="../../img/donacija.png"></div>',
					'<p class="pregleditemdescription"> Redna donacija</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x {{ itemprice }} €</p>',
					'</div>'].join('\n');

var d = new Date();

function getItemIdByName(name) {
	items = JSON.parse($.cookie('dolzniCart2')).items;
	var returner = -1;

	$.each(items, function(i, e) {
		if (e['name'] === name) {
			returner = i;
		}
	});

	return returner;
}

function renderEnkratna(itemprice, itemquantity) {
	return enkratnaHTML.replace('{{ itemprice }}', itemprice).replace('{{ itemquantity }}', itemquantity);
}
function renderRedna(itemprice, itemquantity) {
	return rednaHTML.replace('{{ itemprice }}', itemprice).replace('{{ itemquantity }}', itemquantity);
}

function calculatePrice() {
	items = JSON.parse($.cookie('dolzniCart2')).items;
	var price = 0;
	
	$.each(items, function(i, e) {
		price = price + (parseInt(e['price']) * parseInt(e['quantity']));
	});
    
    $('.paypalprice').val(price);
	
	return price;
}

function renderSummary() {
	items = JSON.parse($.cookie('dolzniCart2')).items;
	
	// dodaj artikle
	$.each(items, function(i, e) {
		if (e['name'].indexOf('donacija') !== -1) {
			if (e['name'].indexOf('Enkratna') != -1) {
				// enkratna je
				enkratnaid = getItemIdByName(e['name']);
				$('.pregledtotal').before(renderEnkratna(items[enkratnaid]['price'], items[enkratnaid]['quantity']));
			} else {
				// redna je
				rednaid = getItemIdByName(e['name']);
                $('.pregledtotal').before(renderRedna(items[rednaid]['price'], items[rednaid]['quantity']));
			}
		}
	});
	
	$('.pregledtotalprice').text(calculatePrice() + ' €');
}

function addItems() {
	items = JSON.parse($.cookie('dolzniCart2')).items;
	
	$.each(items, function(i, e) {
		if (e['name'].indexOf('majica') != -1) {
			// majica je
			var i = 0;
			while (i < parseInt(e['quantity'])) {
				$.post('http://djapi.danesjenovdan.si/nsa/addshopitem', {
					'id': $.cookie('djndid'),
					'name': e['details']['realname'],
					'details': 'Tip: ' + e['details']['type'] + ', velikost: ' + e['details']['size'],
					'payed': 'false',
					'payment_type': 'something',
					'delivery': 'address'
				}, function(r) {
					console.log(r);
				});
				
				i++;
			}
		} else {
			// rizle so
			var i = 0;
			while (i < parseInt(e['quantity'])) {
				$.post('http://djapi.danesjenovdan.si/nsa/addshopitem', {
					'id': $.cookie('djndid'),
					'name': 'Rizle',
					'details': '',
					'payed': 'false',
					'payment_type': 'something',
					'delivery': 'address'
				}, function(r) {
					console.log(r);
				});
				
				i++;
			}
		}
	});
}

var allgood = false;
var payment = false;

var shopObject = {
    'id': $.cookie('djndid'),
    'name': '',
    'details': '',
    'payed': 'false',
    'payment_type': '',
    'delivery': '',
    'address': ''
}

$(document).ready(function() {
	
    if (window.location.href.indexOf('hvala') !== -1) {
        $('.card-vozicek').addClass('hidden');
        $('.vozicek-hvala').removeClass('hidden');
    }
    
	// render summary
	renderSummary();
	
    // donacija (pregled) baton
	$('.btn-donacija-first').on('click', function() {
        
        // ga za donacijo
        if (document.location.href.indexOf('redna') === -1) {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'one_time_d',
                'eventAction': 'step21'
            });
        } else {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'regular_d',
                'eventAction': 'step21'
            });
        }
        
		$(this).parent().addClass('hidden').next().removeClass('hidden');
        $('.vozicekstep.active').removeClass('active').next().addClass('active');
	});
	
	// podatki
    // podatki baton
    $('.btn-donacija-second').on('click', function() {
        $('#narocniknotform input').each(function(i, e) {
            if ($(e).val() != '') {
                if ($(e).data('object') === 'name') {
                    shopObject['address'] = $(e).val() + ' ';
                } else if ($(e).data('object') === 'address') {
                    shopObject['address'] += ' ' + $(e).val();
                } else if ($(e).data('object') === 'address2') {
                    shopObject['address'] += ' ' + $(e).val();
                } else if ($(e).data('object') === 'email') {
                    // do nothing (ignore)
                } else {
                    shopObject[$(e).data('object')] = $(e).val();
                }
                
                allgood = true;

            } else {
                $('#narocniknotform input').shake();
                allgood = false;
                return false;
            }
        });
        
        if (allgood) {
            
            // ga za donacijo
        if (document.location.href.indexOf('redna') === -1) {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'one_time_d',
                'eventAction': 'step22'
            });
        } else {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'regular_d',
                'eventAction': 'step22'
            });
        }
            
            //function updateVictim(id, name, lastname, email, fbid)
            updateVictim(
                $.cookie('djndid'),
                $('#narocniknotform input:first-of-type').val().split(' ')[0],
                $('#narocniknotform input:first-of-type').val().split(' ')[1],
                $('.emailshopinput').val(), ''
            );
            
            shopObject['details'] += '|| ' + $('#narocniknotform textarea').val() + ' || ';
        
            $(this)
                .parent()
                .addClass('hidden')
                .next()
                    .removeClass('hidden');
            $('.vozicekstep.active')
                .removeClass('active')
                .next()
                    .addClass('active');
            
            if (JSON.parse($.cookie('dolzniCart2'))['items'][0]['name'].indexOf('Enkratna') !== -1) {
                $('.mesecnoplacilo').addClass('hidden');
                $('.enkratnoplacilo').removeClass('hidden');
            }
        } else {
            $('#narocniknotform input').shake();
        }
        
    });
    
    // payment type
    $('.placiloform input').on('click', function() {
        shopObject['payment_type'] = $(this).data('object');
    });
    
    $('.btn-placaj').on('click', function() {
        
        // log shop items into database
        $.each(JSON.parse($.cookie('dolzniCart2'))['items'], function(i, e) {
            
            var newShopObject = JSON.parse(JSON.stringify(shopObject));
            
            if (e['name'].indexOf('Enkratna') != -1) {
//                newShopObject['details'] = '';
                newShopObject['name'] = e['name'];
                $('#paypalitemname').val(e['name']);
                
            } else {
                
                newShopObject['name'] = e['name'];
                $('#paypalitemname').val(e['name']);
//                newShopObject['details'] = '';
                
            }
            
            console.log(shopObject, newShopObject);
            
            $.post('http://djapi.danesjenovdan.si/nsa/addshopitem', newShopObject, function(r) {
                console.log(r);
                
                // pošlji mail
                if (e['name'].indexOf('Enkratna') !== -1) {
                    // enkratna donacija
                    
                    if (shopObject['payment_type'].indexOf('paypal') !== -1) {
                        $('#paypalitemname').val('Enkratna donacija ');
                        // paypal
                        $('#paypalformenkrat').submit();
                        window.setTimeout(function() {
                            sendTheMail($('.emailshopinput').val(), enkratnadonacijaHTML);
                        }, 100); 
                    } else {
                        $('.card-vozicek').addClass('hidden');
                        $('.vozicek-hvala').removeClass('hidden');
                        
                        window.setTimeout(function() {
                            sendTheMail($('.emailshopinput').val(), enkratnadonacijaHTML + '<br>P.S.: Če imaš težave pri izpolnjevanju položnice, si svojo oglej <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=666999&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=CHAR&name=' + encodeURIComponent($('#donacijanamelastname').val()) + '&address1=&address2=' + '">tukaj</a>.');
                        }, 100); 
                        
                    }
                    
                } else {
                    // redna donacija
                    window.setTimeout(function() {
                        sendTheMail($('.emailshopinput').val(), rednadonacijaHTML);
                    }, 100); 
                    
                    $('#paypalformredno').submit();
                    
                }
                
                // spucaj vozicek ob uspesnem placilu
                $.removeCookie('dolzniCart2', {'path': '/'});
                // ga za donacijo
                if (document.location.href.indexOf('redna') === -1) {
                    ga('send', {
                        'hitType': 'event',
                        'eventCategory': 'one_time_d',
                        'eventAction': 'step23'
                    });
                } else {
                    ga('send', {
                        'hitType': 'event',
                        'eventCategory': 'regular_d',
                        'eventAction': 'step23'
                    });
                }
            });
            
            
        });
        
    });
	
});