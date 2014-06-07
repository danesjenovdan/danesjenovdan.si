var majicaHTML = [	'<div class="vozicekitemcontainer">',
					'<div class="vozicekitemimage" data-img="http://danesjenovdan.si/styleguide/img/jure.png" style="background-image: url(http://danesjenovdan.si/styleguide/img/jure.png); "></div>',
					'<h1 class="vozicekitemtitle">Majica</h1>',
					'<p class="vozicekitemproperty">{{ itemtype }}</p>',
					'<p class="vozicekitemproperty">velikost {{ itemsize }}</p>',
					'<div class="vozicekitemcountercontainer">',
					'<div class="vozicekitemcounter" data-name="{{ itemname }}"><span class="artikelnumber">{{ itemquantity }}</span><div class="plusone" onclick="addItem($(this).parent().data(\'name\')); renderCart();"></div><div class="minusone" onclick="removeItem(getItemIdByName($(this).parent().data(\'name\'))); renderCart();"></div></div>',
					'<div class="vozicekitemremove" data-name="{{ itemname }}" onclick="removeItemFamily(getItemIdByName($(this).data(\'name\'))); renderCart();">Odstrani <span class="odstranix">×</span></div>',
					'</div>',
					'</div>'].join('\n'); // TODO update picture
					
var rizleHTML = [	'<div class="vozicekitemcontainer">',
					'<div class="vozicekitemimage" data-img="http://danesjenovdan.si/styleguide/img/jure.png" style="background-image: url(http://danesjenovdan.si/styleguide/img/jure.png); "></div>',
					'<h1 class="vozicekitemtitle">Rizle</h1>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<div class="vozicekitemcountercontainer">',
					'<div class="vozicekitemcounter" data-name="{{ itemname }}"><span class="artikelnumber">{{ itemquantity }}</span><div class="plusone" onclick="addItem($(this).parent().data(\'name\')); renderCart();"></div><div class="minusone" onclick="removeItem(getItemIdByName($(this).parent().data(\'name\'))); renderCart();"></div></div>',
					'<div class="vozicekitemremove" data-name="{{ itemname }}" onclick="removeItemFamily(getItemIdByName($(this).data(\'name\'))); renderCart();">Odstrani <span class="odstranix">×</span></div>',
					'</div>',
					'</div>'].join('\n'); // TODO update picture

var racunHTML = [	'<div class="vozicekracunitemcontainer">',
					'<div class="vozicekracunitem">{{ itemname }}</div>',
					'<div class="vozicekracunprice">{{ itemtotalprice }} eur</div>',
					'</div>'].join('\n');



function createCart() {
	$.cookie('dolzniCart', JSON.stringify({'items': []}));
}

function addItem(name, quantity, details, price) {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	if (items.length === 0) { // empty cart
		items.push({'name': name, 'quantity': quantity, 'details': details, 'price': price});

		$.cookie('dolzniCart', JSON.stringify({'items': items}));
	} else { // something already in cart
		$.each(items, function(i, e) {
			if (e['name'] === name) {
				items[i]['quantity'] = parseInt(items[i]['quantity']) + 1;
			
				$.cookie('dolzniCart', JSON.stringify({'items': items}));
				
				return false;
			} else if (i + 1 === items.length){
				items.push({'name': name, 'quantity': quantity, 'details': details, 'price': price});

				$.cookie('dolzniCart', JSON.stringify({'items': items}));
			}
		});
	}
}

function removeItem(id) {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	if (items[id].quantity > 1) {
		items[id]['quantity'] = items[id]['quantity'] - 1;
	} else {
		items.splice(id, 1);
	}
	
	$.cookie('dolzniCart', JSON.stringify({'items': items}));
}

function removeItemFamily(id) {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	items.splice(id, 1);
	
	$.cookie('dolzniCart', JSON.stringify({'items': items}));
}

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

function incrementQuantity(name) {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	items[getItemIdByName(name)]['quantity'] = parseInt(items[getItemIdByName(name)]['quantity'] + 1);
	
	$.cookie('dolzniCart', JSON.stringify({'items': items}));
}

function calculatePrice() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	var price = 0;
	
	$.each(items, function(i, e) {
		price = price + (parseInt(e['price']) * parseInt(e['quantity']));
	});
	
	return price;
}

function countItems() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	var count = 0;
	
	$.each(items, function(i, e) {
		count = count + parseInt(e['quantity']);
	});
	
	return count;
}

function renderMajica(itemtype, itemsize, itemquantity, itemname) {
	return majicaHTML.replace('{{ itemtype }}', itemtype).replace('{{ itemsize }}', itemsize).replace('{{ itemquantity }}', itemquantity).replace(/\{\{ itemname \}\}/g, itemname);
}

function renderRizle(itemquantity, itemname) {
	return rizleHTML.replace('{{ itemquantity }}', itemquantity).replace(/\{\{ itemname \}\}/g, itemname);
}

function renderRacun(itemname, itemtotalprice) {
	return racunHTML.replace('{{ itemname }}', itemname).replace('{{ itemtotalprice }}', itemtotalprice);
}

function renderCart() {
	items = JSON.parse($.cookie('dolzniCart')).items;
	
	if (items.length === 0) {
		$('#row-cart, .vozicek').removeClass('open');
	} else {
		$('#row-cart').addClass('open');
	}
	$('#cartcounter').text(countItems());
	
	// pobriši voziček
	$('.vozicekitemcontainer').remove();
	$('.vozicekracunitemcontainer').remove();

	// dodaj artikle
	$.each(items, function(i, e) {
		if (e['name'].indexOf('donacija') == -1) {
			if (e['name'].indexOf('majica') != -1) {
				// majica je
			
				majicaid = getItemIdByName(e['name']);
				// zgoraj
				$('.vozicekracun').before(renderMajica(items[majicaid]['details']['type'], items[majicaid]['details']['size'], items[majicaid]['quantity'], items[majicaid]['name']));
				// na računu
				$('.vozicekracun').prepend(renderRacun('Majica ' + items[majicaid]['details']['size'] + ' ' + items[majicaid]['details']['type'] + ' kroj', (parseInt(items[majicaid]['quantity']) * parseInt(items[majicaid]['price']))));
			} else {
				// rizle so
			
				rizleid = getItemIdByName(e['name']);
				// zgoraj
				$('.vozicekracun').before(renderRizle(items[rizleid]['quantity'], items[rizleid]['name']));
				// na računu
				$('.vozicekracun').prepend(renderRacun('Rizle', (items[rizleid]['quantity'] * items[rizleid]['price'])));
			}
		}
	});
	
	// končna cena
	$('.vozicekracuntotalprice').text(calculatePrice() + ' eur');
	
}

$(document).ready(function() {

	createCart();

	$('.velikosrcetile').on('click', function() {
		$(this).siblings().each(function(i, e) {
			if ($(e).hasClass('selected')) {
				$(e).removeClass('selected');
			}
		})
		$(this).toggleClass('selected');
		
		// activate button
	});
	
	$('.input-drugo').on('focusout', function() {
		var reg = /^\d+$/;
		if (reg.test($(this).val())) {
			$(this).parent().siblings('.selected').removeClass('selected');
			$(this).parent().addClass('selected');
		} else {
			$(this).parent().shake();
			$(this).removeClass(selected);
		}
	});
	
	$('#submitnaturalije').on('click', function() {
		if ($('#naturalijeemail').val() != '' && $('#naturalijetextarea').val() != '') {
			$.post('https://djnd.slack.com/services/hooks/incoming-webhook?token=EApBJ7B21GFJmytVv5ZoNqoV',
				JSON.stringify({
					'channel': '#api-monitor',
					'username': 'Apinator',
					'text': 'Yo Filip! Nekdo je obljubil naturalije!',
					'attachments': [
						{
							'fallback': 'Your client is stupid, go vote.',
							'color': 'good',
							'parse': 'full',
							'fields': [
								{
									'title': $('#naturalijeemail').val(),
									'value': $('#naturalijetextarea').val(),
									'short': false
								}
							]
						}
					]
				}), 
				function(r) {
					console.log(r);
				}
			);
			$(this).parents('.popup').removeClass('open');
		} else {
			$('.naturalijeform').shake();
		}
	});
	
	$('.btn-finish').on('click', function() {
		if ($(this).parent().parent().children('.artikeltogglecontainer:nth-of-type(1)').children('.artikeltoggle').hasClass('dolzniselected') && $(this).parent().parent().children('.artikeltogglecontainer:nth-of-type(2)').children('.artikeltoggle').hasClass('dolzniselected')) {
			// everything OK
			$(this).parents('.popup').removeClass('open');
		} else {
			$(this).parent().parent().children('.artikeltogglecontainer, .artikellable').not('.noshake').shake();
		}
	});
	
	$('.gallerymainimage, .gallerythumb, .vozicekitemimage, .pregleditemimage').each(function(i, e) {
		$(e).css('background-image', 'url(' + $(e).data('img') + ')');
	});
	$('.gallerythumb').on('click', function() {
		console.log($(this).data('img'));
		$(this).parents('.artikelgallerycontainer').children('.gallerymainimage').css({
			'background-image': 'url(' + $(this).data('img') + ')'
		});
	});
	
	$('#carticons').on('click', function() {
		renderCart();
		$('.vozicek').toggleClass('open');
	});
	
	$('.artikeltoggle').on('click', function() {
		$(this).siblings().each(function(i, e) {
			if ($(e).hasClass('dolzniselected')) {
				$(e).removeClass('dolzniselected');
			}
		})
		$(this).addClass('dolzniselected');
		
		// activate button
	});
	
	// $('.btn-dolzni').not('#submitnaturalije').on('click', function() {
	// 	if (!$(this).siblings('.velikosrcetilecontainer').children().hasClass('selected')) {
	// 		$(this).prev().shake();
	// 	} else {
	// 		// all OK
	// 	}
	// });
	
	$('#submitenkratna').on('click', function() {
		if (!$(this).siblings('.velikosrcetilecontainer').children().hasClass('selected')) {
			$(this).prev().shake();
		} else {
			// all OK
			if ($(this).prev().children('.selected').hasClass('velikosrceinput')) {
				addItem('Enkratna donacija ' + $(this).prev().children('.selected').children('.input-drugo').val() + ' eur', 1, '', $(this).prev().children('.selected').children('.input-drugo').val());
			} else {
				addItem('Enkratna donacija ' + $(this).prev().children('.selected').text().split(' ')[0] + ' eur', 1, '', $(this).prev().children('.selected').text().split(' ')[0]);
			}
		}
	});

	$('#submitredna').on('click', function() {
		if (!$(this).siblings('.velikosrcetilecontainer').children().hasClass('selected')) {
			$(this).prev().shake();
		} else {
			// all OK
			if ($(this).prev().children('.selected').hasClass('velikosrceinput')) {
				addItem('Redna donacija ' + $(this).prev().children('.selected').children('.input-drugo').val() + ' eur', 1, '', $(this).prev().children('.selected').children('.input-drugo').val());
			} else {
				addItem('Redna donacija ' + $(this).prev().children('.selected').text().split(' ')[0] + ' eur', 1, '', $(this).prev().children('.selected').text().split(' ')[0]);
			}
		}
	});
	
	// add item to cart
	$('.artikelfinishorlink').on('click', function() {
		
		window.setTimeout(function() {
			renderCart();
		}, 500);
		
		// determine what it's for
		if ($(this).parents('.popup').attr('id') === 'majicapopup') {
			// majica
			
			if ($(this).parent().parent().parent().children('.artikeltogglecontainer:nth-of-type(1)').children('.artikeltoggle').hasClass('dolzniselected') && $(this).parent().parent().parent().children('.artikeltogglecontainer:nth-of-type(2)').children('.artikeltoggle').hasClass('dolzniselected')) {
				// everything OK
				
				// generate data
				var name = 'majica';
				if ($(this).parent().parent().siblings('.majicatype').children('.dolzniselected').text() === 'ohlapen') {
					name = name + 'oh' + $(this).parent().parent().siblings('.majicasize').children('.dolzniselected').text();
				} else {
					name = name + 'op' + $(this).parent().parent().siblings('.majicasize').children('.dolzniselected').text();
				}
				var quantity = $(this).parent().parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
				var details = {
					'realname': 'Majica',
					'type': $(this).parent().parent().siblings('.majicatype').children('.dolzniselected').text(),
					'size': $(this).parent().parent().siblings('.majicasize').children('.dolzniselected').text()
				}

				// add item
				addItem(name, quantity, details, 12);
				
				$(this).parents('.popup').removeClass('open');

			} else {
				$(this).parent().parent().parent().children('.artikeltogglecontainer, .artikellable').not('.noshake').shake();

			}

			return false;
			
		} else {
			// ker ni drugega morajo bit rizle
			// generate data
			var name = 'rizle'
			var quantity = $(this).parent().parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
			var details = {}
			
			// add item
			addItem(name, quantity, details, 2);
			
			$(this).parents('.popup').removeClass('open');
			
			return false;
		}
		
	});
	
	// plus/minus
	$('.plusone').on('click', function() {
		$(this).siblings('.artikelnumber').text((parseInt($(this).siblings('.artikelnumber').text()) + 1));
	})
	$('.minusone').on('click', function() {
		if ($(this).siblings('.artikelnumber').text() != '1') {
			$(this).siblings('.artikelnumber').text((parseInt($(this).siblings('.artikelnumber').text()) - 1));
		}
	})
	
	
});