var majicaHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/majica1.jpg);" data-img="../../img/majica1.jpg"></div>',
					'<p class="pregleditemdescription"> Majica / {{ itemtype }} / {{ itemsize }}</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x 12 €</p>',
					'</div>'].join('\n');
var rizleHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/rizle1.jpg);" data-img="../../img/rizle1.jpg"></div>',
					'<p class="pregleditemdescription"> Rizle</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x 2 €</p>',
					'</div>'].join('\n');

var billitems = '';
var majicainbasket = false;
var rizleinbasket = false;

var d = new Date();

function getItemIdByName(name) {
	items = JSON.parse($.cookie('dolzniCart')).items;
	var returner = -1;

	$.each(items, function(i, e) {
		if (e['name'] === name) {
			returner = i;
		}
	});

	return returner;
}

function renderMajica(itemtype, itemsize, itemquantity) {
	return majicaHTML.replace('{{ itemtype }}', itemtype).replace('{{ itemsize }}', itemsize).replace('{{ itemquantity }}', itemquantity);
}
function renderRizle(itemquantity) {
	return rizleHTML.replace('{{ itemquantity }}', itemquantity);
}

function calculatePrice() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	var price = 0;
	
	$.each(items, function(i, e) {
		price = price + (parseInt(e['price']) * parseInt(e['quantity']));
	});
	
    $('#paypalprice').val(price);
	return price;
}

function renderSummary() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	// dodaj artikle
	$.each(items, function(i, e) {
		if (e['name'].indexOf('donacija') == -1) {
			if (e['name'].indexOf('majica') != -1) {
				// majica je
				majicaid = getItemIdByName(e['name']);
				$('.pregledtotal').before(renderMajica(items[majicaid]['details']['type'], items[majicaid]['details']['size'], items[majicaid]['quantity']));
                
                $('#paypalitemname').val($('#paypalitemname').val() + ' Majica');
			} else {
				// rizle so
				rizleid = getItemIdByName(e['name']);
				$('.pregledtotal').before(renderRizle(items[rizleid]['quantity']));
                
                $('#paypalitemname').val($('#paypalitemname').val() + ' Rizle');
			}
		}
	});
	
	$('.pregledtotalprice').text(calculatePrice() + ' €');
}

function addItems() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
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
	
    // pregled baton
	$('.btn-pregled-first').on('click', function() {
        
        // ga za vozicek
        if (document.location.href.indexOf('#checkout') === -1) {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'vozicek',
                'eventAction': 'step31'
            });
        } else {
            ga('send', {
                'hitType': 'event',
                'eventCategory': 'vozicek',
                'eventAction': 'step21'
            });
        }
        
		$(this).parent().addClass('hidden').next().removeClass('hidden');
        $('.vozicekstep.active').removeClass('active').next().addClass('active');
	});
	
	// prevzem
	$('#osebno').on('click', function() {
		$('#osebnoform').removeClass('hidden');
        $('#narocniknotform h1').text('Kdo pride po robo?');
        $('#placajpopovzetju').parent().addClass('hidden');
        allgood = false;
	});
	$('#poposti').on('click', function() {
		$('#narocniknotform').removeClass('hidden');
        $('#osebnoform').addClass('hidden');
        $('#narocniknotform h1').text('Kam pošljemo?');
        $('#placajpopovzetju').parent().removeClass('hidden');
        shopObject['delivery'] = 'po pošti';
        allgood = true;
	});
	$('#hekovnik, #lendava, #pina, #bikofe').on('click', function() {
		$('#narocniknotform').removeClass('hidden');
        shopObject['delivery'] = 'dvigne ' + $(this).data('object');
        allgood = true;
	});
    
    // prevzem baton
    $('.btn-prevzem').on('click', function() {
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
            
            // ga za vozicek
            if (document.location.href.indexOf('#checkout') === -1) {
                ga('send', {
                    'hitType': 'event',
                    'eventCategory': 'vozicek',
                    'eventAction': 'step32'
                });
            } else {
                ga('send', {
                    'hitType': 'event',
                    'eventCategory': 'vozicek',
                    'eventAction': 'step22'
                });
            }
            
            //function updateVictim(id, name, lastname, email, fbid)
            updateVictim($.cookie('djndid'), $('#narocniknotform input:first-of-type').val().split(' ')[0], $('#narocniknotform input:first-of-type').val().split(' ')[1], $('.emailshopinput').val(), '');
            
            shopObject['details'] += '|| ' + $('#narocniknotform textarea').val() + ' || ';
        
            $(this).parent().addClass('hidden').next().removeClass('hidden');
            $('.vozicekstep.active').removeClass('active').next().addClass('active');
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
        $.each(JSON.parse($.cookie('dolzniCart'))['items'], function(i, e) {
            
            var newShopObject = JSON.parse(JSON.stringify(shopObject));
            
            if (e['name'].indexOf('majica') != -1) {
                // majica je
                
                majicainbasket = true;
                
                newShopObject['details'] += 'velikost: ' + e['details']['size'] + ', kroj: ' + e['details']['type'] + ' količina: ' + e['quantity'];
                newShopObject['name'] = e['details']['realname'];
                
            } else {
                
                rizleinbasket = true;
                
                newShopObject['name'] = 'Rizle';
                newShopObject['details'] += 'količina: ' + e['quantity'];
                
            }
            
            console.log(shopObject, newShopObject);
            
            $.post('http://djapi.danesjenovdan.si/nsa/addshopitem', newShopObject, function(r) {
                console.log(r);
                
                // handle bill
                console.log('i ' + i);
                console.log(JSON.parse($.cookie('dolzniCart'))['items'].length - 1);
                if (i < JSON.parse($.cookie('dolzniCart'))['items'].length - 1) {
                    billitems += ' ' + r;
                } else {
                    billitems += ' ' + r;
                    $.post('http://djapi.danesjenovdan.si/nsa/addbill', {
                        'price': $('#paypalprice').val(),
                        'itemids': billitems
                    }, function(response) {
                        console.log(response);
                        
                        // račun je pripravljen, itemi so oddani, čas je za plačilo
                        if (shopObject['delivery'].indexOf('dvigne') === -1) {
                            
                            // ne dvigne
                            switch(shopObject['payment_type']) {
                                case 'paypal':
                                    // pošlji mail
                                    if (majicainbasket) {
                                        if (rizleinbasket) {
                                            // majica in rizle
                                            window.setTimeout(function() {
                                                mailHTML = paypalvseHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        } else {
                                            // samo majica
                                            window.setTimeout(function() {
                                                mailHTML = paypalmajicaHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        }
                                    } else {
                                        // samo rizle
                                        window.setTimeout(function() {
                                            mailHTML = paypalrizleHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                            sendTheMail($('.emailshopinput').val(), mailHTML);
                                        }, 100);
                                    }
                                
                                    // plačaj
                                    $('#paypalform').submit();
                                    break;
                                case 'po povzetju':
                                    // pošlji mail
                                    if (majicainbasket) {
                                        if (rizleinbasket) {
                                            // majica in rizle
                                            window.setTimeout(function() {
                                                mailHTML = popovzetjuvseHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        } else {
                                            // samo majica
                                            window.setTimeout(function() {
                                                mailHTML = popovzetjumajicaHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        }
                                    } else {
                                        // samo rizle
                                        window.setTimeout(function() {
                                            mailHTML = popovzetjurizleHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                            sendTheMail($('.emailshopinput').val(), mailHTML);
                                        }, 100);
                                    }
                                    
                                    // odpri zahvalo
                                    $('.card-vozicek').addClass('hidden');
                                    $('.vozicek-hvala').removeClass('hidden');
                                
                                    break;
                                case 'poloznica':
                                    // pošlji mail
                                    if (majicainbasket) {
                                        if (rizleinbasket) {
                                            // majica in rizle
                                            window.setTimeout(function() {
                                                
                                                mailHTML = poloznicavseHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P. S. Če imaš težave pri izpolnjevanju položnice, si svojo oglej <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        } else {
                                            // samo majica
                                            window.setTimeout(function() {
                                                mailHTML = poloznicamajicaHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P. S. Če imaš težave pri izpolnjevanju položnice, si svojo oglej <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                                
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        }
                                    } else {
                                        // samo rizle
                                        window.setTimeout(function() {
                                            
                                            mailHTML = poloznicarizleHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P.P.S.: Da ne bo težav pri izpolnjevanju položnice, je vzorec <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                            
                                            sendTheMail($('.emailshopinput').val(), mailHTML);
                                        }, 100);
                                    }
                                    
                                    // odpri zahvalo
                                    $('.card-vozicek').addClass('hidden');
                                    $('.vozicek-hvala').removeClass('hidden');
                                    
                                    break;
                            }
                        } else {
                            switch(shopObject['payment_type']) {
                                case 'paypal':
                                    // pošlji mail
                                    if (majicainbasket) {
                                        if (rizleinbasket) {
                                            // majica in rizle
                                            window.setTimeout(function() {
                                                mailHTML = paypalvsedvignemHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        } else {
                                            // samo majica
                                            window.setTimeout(function() {
                                                mailHTML = paypalmajicadvignemHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        }
                                    } else {
                                        // samo rizle
                                        window.setTimeout(function() {
                                            mailHTML = paypalrizledvignemHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response);
                                            sendTheMail($('.emailshopinput').val(), mailHTML);
                                        }, 100);
                                    }
                                
                                    // plačaj
                                    $('#paypalform').submit();
                                    break;
                                    
                                case 'poloznica':
                                    // pošlji mail
                                    if (majicainbasket) {
                                        if (rizleinbasket) {
                                            // majica in rizle
                                            window.setTimeout(function() {
                                                
                                                mailHTML = poloznicavsedvignemHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P.P.S.: Da ne bo težav pri izpolnjevanju položnice, je vzorec <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                                
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        } else {
                                            // samo majica
                                            window.setTimeout(function() {
                                                
                                                mailHTML = poloznicamajicadvignemHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P.P.S.: Da ne bo težav pri izpolnjevanju položnice, je vzorec <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                                
                                                sendTheMail($('.emailshopinput').val(), mailHTML);
                                            }, 100);
                                        }
                                    } else {
                                        // samo rizle
                                        window.setTimeout(function() {
                                            mailHTML = poloznicarizledvignemHTMLHTML + racunHTML.replace('{{ id }}', response).replace('{{ id2 }}', response) + '<br>P.P.S.: Da ne bo težav pri izpolnjevanju položnice, je vzorec <a href="http://djapi.danesjenovdan.si/nsa/poloznica?id=' + response + '&date=' + encodeURIComponent(d.getDate() + '.' + d.getMonth() + '.' + d.getFullYear()) + '&price=' + $('.pregledtotalprice').text().split(' ')[0] + '&code=TRAD&name=' + encodeURIComponent($('#voziceknamelastname').val()) + '&address1=' + $('#vozicekaddress1').val() + '&address2=' + $('#vozicekaddress2').val() + '">tukaj</a>.';
                                            
                                            sendTheMail($('.emailshopinput').val(), mailHTML);
                                        }, 100);
                                    }
                                
                                    // odpri zahvalo
                                    $('.card-vozicek').addClass('hidden');
                                    $('.vozicek-hvala').removeClass('hidden');
                                    
                                    break;
                                }
                        }     
                        // spucaj vozicek ob uspesnem placilu
                        $.cookie('dolzniCart', JSON.stringify({'items': []}), {'path': '/'});
                        // ga za vozicek
                        if (document.location.href.indexOf('#checkout') === -1) {
                            ga('send', {
                                'hitType': 'event',
                                'eventCategory': 'vozicek',
                                'eventAction': 'step33'
                            });
                        } else {
                            ga('send', {
                                'hitType': 'event',
                                'eventCategory': 'vozicek',
                                'eventAction': 'step23'
                            });
                        }
                    });
                }
                
            });
            
            
        });
        
    });
	
});