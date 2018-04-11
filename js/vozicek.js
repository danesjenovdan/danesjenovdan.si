var majicaHTML = [  '<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/majica1.jpg);" data-img="../../img/majica1.jpg"></div>',
					'<p class="pregleditemdescription"> Majica / {{ itemtype }} / {{ itemsize }}</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x {{ price }} €</p>',
					'</div>'].join('\n');
var rizleHTML = [   '<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/rizle1.jpg);" data-img="../../img/rizle1.jpg"></div>',
					'<p class="pregleditemdescription"> Rizle</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x {{ price }} €</p>',
					'</div>'].join('\n');
var salcaHTML = [   '<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(../../img/salca1.jpg);" data-img="../../img/salca1.jpg"></div>',
					'<p class="pregleditemdescription"> Šalčka</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x {{ price }} €</p>',
					'</div>'].join('\n');

var billitems = '';
var majicainbasket = false;
var rizleinbasket = false;
var salcainbasket = false;

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

function renderMajica(itemtype, itemsize, itemquantity, price) {
	return majicaHTML.replace('{{ itemtype }}', itemtype).replace('{{ itemsize }}', itemsize).replace('{{ itemquantity }}', itemquantity).replace(/{{ price }}/g, price);
}
function renderRizle(itemquantity, price) {
	return rizleHTML.replace('{{ itemquantity }}', itemquantity).replace(/{{ price }}/g, price);
}
function renderSalca(itemquantity, price) {
	return salcaHTML.replace('{{ itemquantity }}', itemquantity).replace(/{{ price }}/g, price);
}
function calculatePrice() {
	var price = 0;

	$.each(basket_items, function(i, e) {
		if (e['article']['name'].indexOf('donacija') === -1) {
			price = price + (parseInt(e['article']['price']) * parseInt(e['quantity']));
		}
	});
	console.log(price)
	return price;
}

function renderSummary() {
	// dodaj artikle
	$.each(basket_items, function(i, e) {
		if (e['article']['name'].indexOf('donacija') == -1) {
			if (e['article']['name'].indexOf('Majica') != -1) {
				// majica je
				words = e['article']['name'].split("-")
				gen = words[1]
				size = words[2]

				if(gen === "m"){
					type = "moški"
				}
				else{
					type = "ženski"
				}
				$('.pregledtotal').before(renderMajica(type, size, e['quantity'], parseInt(e['article']['price'])));

				$('#paypalitemname').val($('#paypalitemname').val() + ' Majica');
			} else if (e['article']['name'].indexOf('Rizle') != -1) {
				// rizle so
				$('.pregledtotal').before(renderRizle(e['quantity'], parseInt(e['article']['price'])));

				$('#paypalitemname').val($('#paypalitemname').val() + ' Rizle');
			} else {
				// salca je
				$('.pregledtotal').before(renderSalca(e['quantity'], parseInt(e['article']['price'])));

				$('#paypalitemname').val($('#paypalitemname').val() + ' Šalčka');
			}
		}
	});

	$('.pregledtotalprice').text(calculatePrice() + ' €');
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
			//updateVictim($.cookie('djndid'), $('#narocniknotform input:first-of-type').val().split(' ')[0], $('#narocniknotform input:first-of-type').val().split(' ')[1], $('.emailshopinput').val(), '');

			
			costumer_data['name'] = $('#narocniknotform input:first-of-type').val()
			costumer_data['address'] = $("#vozicekaddress1").val() + ", " + $("#vozicekaddress2").val()
			costumer_data['phone'] = 00
			costumer_data['email'] = $('.emailshopinput').val()
			if( shopObject['delivery'] == "po pošti" ){
				costumer_data['delivery_method'] = "post";
			}
			else {
				costumer_data['delivery_method'] = "personal_takeover";
			}

			// shopObject['details'] += '|| ' + $('#narocniknotform textarea').val() + ' || ';
			costumer_data['info'] = $('#narocniknotform textarea').val()

			// costumer_data['payment_type']
			// costumer_data['subscription'] = false
			

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

	// NEW CHECKOUT
	$('.btn-placaj').on('click', function() {
		key = $.cookie()["basket"];

		// UPN
		if( $("input:radio[id ='placajspoloznico']:checked").val() == 'on' ){
			costumer_data["payment_type"] = "upn"
			$.ajax({
				type: "POST",
				url: "https://shop.knedl.si/api/checkout/?order_key=" + key,
				data: JSON.stringify(costumer_data),
				dataType: "json",
				success: function(data) {
					console.log('sem poslu checkout');
					console.log(data);
					$.ajax({
						type: "POST",
						url: "https://shop.knedl.si/poloznica/",
						data: JSON.stringify(data),
						dataType: "html",
						success: function(data) {
							console.log('dobu sem poloznco');
							console.log(data);
							$(".vozicekhtml").html(data);
							$.removeCookie('basket', {"path": "/"});
						},
					});
					$.removeCookie('basket', {"path": "/"});
				}
			});
		}
		// PAYPAL
		else if ($("input:radio[id ='placajspaypalom']:checked").val() == 'on') {
			costumer_data["payment_type"] = "paypal";
			costumer_data["subscription"] = false;
			costumer_data["success_url"] = "https://danesjenovdan.si/dolzni/dolzni/?success=true";
			costumer_data["fail_url"] = "https://danesjenovdan.si/dolzni/?success=false&order_key=" + key;
			$.ajax({
				type: "POST",
				url: "https://shop.knedl.si/api/checkout/?order_key=" + key,
				data: JSON.stringify(costumer_data),
				dataType: "json",
				success: function(data) {
					console.log(data);
					$.removeCookie('basket', {"path": "/"});
					window.location.replace(data["redirect_url"])
				}
			});
		}

	});
});
var basket_items = []
var costumer_data = {}

function getBasketKey() {
	console.log("get key")
    basket = $.cookie()["basket"]
    if(basket === undefined || basket === "") {
        console.log("about to get")
        $.get('https://shop.knedl.si/api/basket/', function(data) {
            console.log("key: " + data.order_key)
            $.cookie("basket", data.order_key, {"path": "/", "expires": 10})
            getBasketItems(data.order_key)
        });
    } else {
        getBasketItems(basket);
    }
}
function getBasketItems(key){
    $.get("https://shop.knedl.si/api/items/?order_key=" + key, function(data) {
        basket_items = data;
        renderSummary();
        console.log("rerender")
        $(".overlay, .lds-heart").hide()
    });
}
getBasketKey()