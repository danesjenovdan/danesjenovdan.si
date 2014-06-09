var majicaHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(http://danesjenovdan.si/styleguide/img/jure.png);" data-img="http://danesjenovdan.si/styleguide/img/jure.png"></div>',
					'<p class="pregleditemdescription"> Majica / {{ itemtype }} / {{ itemsize }}</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x 12 eur</p>',
					'</div>'].join('\n');
var rizleHTML = [	'<div class="pregleditemcontainer">',
					'<div class="pregleditemimage" style="background-image: url(http://danesjenovdan.si/styleguide/img/jure.png);" data-img="http://danesjenovdan.si/styleguide/img/jure.png"></div>',
					'<p class="pregleditemdescription"> Rizle</p>',
					'<p class="pregleditemprice">{{ itemquantity }} x 2 eur</p>',
					'</div>'].join('\n');

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
			} else {
				// rizle so
				rizleid = getItemIdByName(e['name']);
				$('.pregledtotal').before(renderRizle(items[rizleid]['quantity']));
			}
		}
	});
	
	$('.pregledtotalprice').text(calculatePrice() + ' eur');
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


$(document).ready(function() {
	
	// redner summary
	renderSummary();
	
	$('.btn-pregled').on('click', function() {
		$(this).parent().addClass('hidden').next().removeClass('hidden');
	});
	
	// prevzem
	$('#osebno').on('click', function() {
		$('#osebnoform').removeClass('hidden');
        $('#narocniknotform h1').text('Kako te identificiramo?');
	});
	$('#poposti').on('click', function() {
		$('#narocniknotform').removeClass('hidden');
        $('#osebnoform').addClass('hidden');
        $('#narocniknotform h1').text('Kam pošljemo?');
	});
	$('#hekovnik, #lendava').on('click', function() {
		$('#narocniknotform').removeClass('hidden');
	});
	
});