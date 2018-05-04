var majicaHTML = [	'<div class="vozicekitemcontainer">',
					'<div class="vozicekitemimage" data-img="../../img/majica1.jpg" style="background-image: url(../../img/majica1.jpg); "></div>',
					'<h1 class="vozicekitemtitle">Majica</h1>',
					'<p class="vozicekitemproperty">{{ itemtype }}</p>',
					'<p class="vozicekitemproperty">velikost {{ itemsize }}</p>',
					'<div class="vozicekitemcountercontainer">',
					'<div class="vozicekitemcounter" data-name="{{ itemname }}"><span class="artikelnumber">{{ itemquantity }}</span><div class="plusone" onclick="addItem({{ itemid }}); renderCart();"></div><div class="minusone" onclick="removeItem({{ itemid }});"></div></div>',
					'<div class="vozicekitemremove" data-name="{{ itemname }}" onclick="removeItemFamily({{ itemid }}); renderCart();">Odstrani <span class="odstranix">×</span></div>',
					'</div>',
					'</div>'].join('\n'); // TODO update picture

var rizleHTML = [	'<div class="vozicekitemcontainer">',
					'<div class="vozicekitemimage" data-img="../../img/rizle1.jpg" style="background-image: url(../../img/rizle1.jpg); "></div>',
					'<h1 class="vozicekitemtitle">Rizle</h1>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<div class="vozicekitemcountercontainer">',
					'<div class="vozicekitemcounter" data-name="{{ itemname }}"><span class="artikelnumber">{{ itemquantity }}</span><div class="plusone" onclick="addItem({{ itemid }}); renderCart();"></div><div class="minusone" onclick="removeItem({{ itemid }});"></div></div>',
					'<div class="vozicekitemremove" data-name="{{ itemname }}" onclick="removeItemFamily({{ itemid }}); renderCart();">Odstrani <span class="odstranix">×</span></div>',
					'</div>',
					'</div>'].join('\n'); // TODO update picture

var salckaHTML = [	'<div class="vozicekitemcontainer">',
					'<div class="vozicekitemimage" data-img="../../img/salca1.jpg" style="background-image: url(../../img/salca1.jpg); "></div>',
					'<h1 class="vozicekitemtitle">Šalčka</h1>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<p class="vozicekitemproperty">&nbsp;</p>',
					'<div class="vozicekitemcountercontainer">',
					'<div class="vozicekitemcounter" data-name="{{ itemname }}"><span class="artikelnumber">{{ itemquantity }}</span><div class="plusone" onclick="addItem({{ itemid }}); renderCart();"></div><div class="minusone" onclick="removeItem({{ itemid }});"></div></div>',
					'<div class="vozicekitemremove" data-name="{{ itemname }}" onclick="removeItemFamily({{ itemid }}); renderCart();">Odstrani <span class="odstranix">×</span></div>',
					'</div>',
					'</div>'].join('\n'); // TODO update picture

var racunHTML = [	'<div class="vozicekracunitemcontainer">',
					'<div class="vozicekracunitem">{{ itemname }}</div>',
					'<div class="vozicekracunprice">{{ itemtotalprice }} €</div>',
					'</div>'].join('\n');


function updateItem(id, quantity) {
	key = $.cookie()["basket"];
	console.log(key)
	$.ajax({
	  type: "PUT",
	  url: "https://shop.djnd.si/api/items/"+ id +"/?order_key=" + key,
	  data: {"quantity": parseInt(quantity)},
	  success: function(data) {
		console.log(data)
		getBasketItems(key);
	  },
	  dataType: "json"
	});
}

function addItem(id, quantity) {
	console.log("update item " + quantity)
	$.each(basket_items, function(i, e) {
		if(e['id'] === id) {
			if(quantity == null){
				quantity = 1
			}
			new_quantity = e['quantity'] + quantity;
			updateItem(id, new_quantity)
		}
	});
}

function removeItem(id, quantity) {
	$.each(basket_items, function(i, e) {
		if(e['id'] === id) {
			if(quantity == null){
				quantity = -1
			}
			// dont remove all items
			if (e['quantity'] > 1) {
				new_quantity = e['quantity'] + quantity;
				updateItem(id, new_quantity)
			}
		}
	});
}

function removeItemFamily(id) {
	/*items = JSON.parse($.cookie('dolzniCart')).items;

	items.splice(id, 1);

	$.cookie('dolzniCart', JSON.stringify({'items': items}), {'expires': 30, 'path': '/'});*/
	key = $.cookie()["basket"];
	console.log(basket_items);
	$.ajax({
		type: "DELETE",
		url: "https://shop.djnd.si/api/items/"+ id +"/?order_key=" + key,
		success: function(data) {
			console.log(data);
			getBasketItems(key);
		},
		dataType: "json"
	});
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

	$.cookie('dolzniCart', JSON.stringify({'items': items}), {'expires': 30, 'path': '/'});
}

function calculatePrice() {
	var price = 0;

	$.each(basket_items, function(i, e) {
		if (e['article']['name'].indexOf('donacija') === -1) {
			price = price + (parseInt(e['article']['price']) * parseInt(e['quantity']));
		}
	});

	return price;
}

function countItems() {
	var count = 0;

	$.each(basket_items, function(i, e) {
		if (e['article']['name'].indexOf('donacija') === -1) {
			count = count + (parseInt(e['quantity']));
		}
	});

	return count;
}

function renderMajica(itemtype, itemsize, itemquantity, itemname, itemid) {
	return majicaHTML.replace('{{ itemtype }}', itemtype).replace('{{ itemsize }}', itemsize).replace('{{ itemquantity }}', itemquantity).replace(/\{\{ itemname \}\}/g, itemname).replace(/{{ itemid }}/g, itemid);
}

function renderRizle(itemquantity, itemname, itemid) {
	return rizleHTML.replace('{{ itemquantity }}', itemquantity).replace(/\{\{ itemname \}\}/g, itemname).replace(/{{ itemid }}/g, itemid);
}

function renderSalcka(itemquantity, itemname, itemid) {
	return salckaHTML.replace('{{ itemquantity }}', itemquantity).replace(/\{\{ itemname \}\}/g, itemname).replace(/{{ itemid }}/g, itemid);
}

function renderRacun(itemname, itemtotalprice) {
	return racunHTML.replace('{{ itemname }}', itemname).replace('{{ itemtotalprice }}', itemtotalprice);
}

function renderCart() {

	if (basket_items.length === 0) {
		$('#row-cart, .vozicek').removeClass('open');
	} else {
		$('#row-cart').addClass('open');
	}

	// pobriši voziček
	$('.vozicekitemcontainer').remove();
	$('.vozicekracunitemcontainer').remove();

	// dodaj artikle
	$.each(basket_items, function(i, e) {
		if (e['article']['name'].indexOf('donacija') == -1) {
			if (e['article']['name'].indexOf('Majica') != -1) {
				// majica je

				// majicaid = getItemIdByName('majica');

				words = e['article']['name'].split("-")
				gen = words[1]
				size = words[2]

				if(gen === "m"){
					type = "moški"
				}
				else{
					type = "ženski"
				}

				// zgoraj
				$('.vozicekracun').before(renderMajica(type, size.toUpperCase(), e['quantity'], "Majica", e["id"]));
				// na računu
				$('.vozicekracun').prepend(renderRacun('Majica ' + size.toUpperCase() + ' ' + type + ' kroj', (parseInt(e['quantity']) * parseInt(e['article']['price']))));
			} else if (e['article']['name'].indexOf('Rizle') != -1) {
				// rizle so

				// rizleid = getItemIdByName(e['article']['name']);
				// zgoraj
				$('.vozicekracun').before(renderRizle(e['quantity'], "Rizle", e["id"]));
				// na računu
				$('.vozicekracun').prepend(renderRacun('Rizle', (e['quantity'] * e['article']['price'])));
			} else {
				// salcaid = getItemIdByName(e['article']['name']);
				$('.vozicekracun').before(renderSalcka(e['quantity'], "Šalčka", e["id"]));
				$('.vozicekracun').prepend(renderRacun('Šalčka', (e['quantity'] * e['article']['price'])));
			}
		}
	});
	// končna cena
	$('.vozicekracuntotalprice').text(calculatePrice() + ' €');

}
function getBasketKey() {
    basket = $.cookie()["basket"]
    if(basket === undefined || basket === "") {
        console.log("about to get")
        $.get('https://shop.djnd.si/api/basket/', function(data) {
            console.log("key: " + data.order_key)
            $.cookie("basket", data.order_key, {"path": "/", "expires": 10})
            getBasketItems(data.order_key)
        });
    } else {
        getBasketItems(basket);
    }
}
function getBasketItems(key){
    $.get("https://shop.djnd.si/api/items/?order_key=" + key, function(data) {
        basket_items = data;
        if($(".vozicek").hasClass("open")){
            // rerender open cart
            renderCart();
            console.log("rerender")
        }
        $('#cartcounter').text(countItems());
        renderCart();
    });
}
function addToCart(itemId, quantity, callback) { // TODO
    key = $.cookie()["basket"]
    console.log({"product_id": itemId, "quantity": parseInt(quantity)})
    console.log("https://shop.djnd.si/api/add_to_basket/?order_key=" + key)
    $.ajax({
        type: "POST",
        url: "https://shop.djnd.si/api/add_to_basket/?order_key=" + key,
        data: JSON.stringify({"product_id": itemId, "quantity": parseInt(quantity)}),
        success: function(data) {
            getBasketItems(data.order_key)
        },
		dataType: "json",
		success: callback(),
	});
}
function selectDonation(price, isSubscription) {
    // get new chart
    donationArticle = articles["enkratna donacija"]
    $.get('https://shop.djnd.si/api/basket/', function(data) {
        donation_order_key = data.order_key
        $.ajax({
          type: "POST",
          url: "https://shop.djnd.si/api/add_to_basket/?order_key=" + donation_order_key,
          data: JSON.stringify({"product_id": donationArticle["id"], "quantity": parseInt(price)}),
          success: function(data) {
            $.cookie("donation", JSON.stringify({"key": donation_order_key, "isSubscription": isSubscription}), {"path": "/", "expires": 10})
          },
          dataType: "json"
        });

    });
}
var basket_items = []
var all_shirts = ['.shirt-xxl', '.shirt-xl', '.shirt-l', '.shirt-m', '.shirt-s'];
var shirts = {"m":[], "z":[]}
var articles = {}
$(document).ready(function() {
	var url_string = window.location.href
	var url = new URL(url_string);
	var success = url.searchParams.get("success");
	if(success=='true'){
		startConfetti();
	}
	else if(success=='false'){
		var order_key = url.searchParams.get("order_key");
		// donation redirect
		if(url.searchParams.get("donacija")=="true") {
			// donation fail
		}
		console.log("try again")

		$.cookie("basket", order_key, {"path": "/", "expires": 10})
	}
	Array.prototype.diff = function(a) {
        return this.filter(function(i) {return a.indexOf(i) < 0;});
    };

    console.log(all_shirts)
    console.log("ivan")

    $.get('https://shop.djnd.si/api/products/', function(data){
        console.log(data);
        $.each(data, function(index, item){
            if (item.name.indexOf("Majica") !== -1){
                if (item.stock > 0) {
                    words = item.name.split("-")
                    gen = words[1]
                    size = words[2]
                    shirts[gen].push(".shirt-"+size)

                    articles[item.name.toLowerCase()] = item.id
                }
            }
            key = item.name.toLowerCase().replace("š","s").replace("č","c").replace("ž","z")
            articles[key] = item
        });
    });
    console.log(shirts)


    $(".btn-finish, .artikelfinishorlink").on("click", function(){
        if($( this ).hasClass("majica")) {
            // check shirt size
            var console_div = null
            console.log("majca", $(this))
            if ($( this ).hasClass("artikelfinishorlink")){
                console_div = $(this).parent().parent()
            }
            else{
                console_div = $(this).parent()
            }
            var size = console_div.siblings('.majicasize').children('.dolzniselected').text();
            var type = console_div.siblings('.majicatype').children('.dolzniselected').text();
            console.log("asdsadasd" + size+" "+type)
            if (type == '' || size == '') {
            	$(this).parent().shake();
            	return
            }
            if (type.indexOf("moški") !== -1){
                type = "m"
            }
            else {
                type = "z"
            }
            key = 'majica-'+type+'-'+size.toLowerCase()
        }
        else if($( this ).hasClass("salcka")) {
            console.log("salca")
            key = "salcka"
        }
        else if($( this ).hasClass("rizle")) {
            key = "rizle"
        }
        console.log("key je " + key)
        console.log(articles[key])
        if ($( this ).hasClass("btn")){
            quantity = $(this).parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text()
        }
        else{
            quantity = $(this).parent().parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text()
        }
        $(this).parents('.popup').removeClass('open');
        if ($( this ).hasClass("btn")){
            //window.open('vozicek#checkout', '_blank');
            addToCart(articles[key].id, quantity, function() {
				document.location.href='/dolzni/vozicek';
			});
        } else {
			addToCart(articles[key].id, quantity, function() {
				console.log('added to cart');
			})
		}
    });
    getBasketKey();

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

	$('#naturalijetextarea').on('focus', function() {
		if ($(this).val() === 'programiranje, analiza podatkov, statistika, vizuzalizacije, aktivizem, pravo, pisarna, blablabla') {
			$(this).val('');
		}
	});

	$('#submitnaturalije').on('click', function() {
		if ($('#naturalijeemail').val() != '' && $('#naturalijetextarea').val() != '') {
			$.ajax({
				type: "POST",
				url: "https://shop.djnd.si/api/send_as_email/",
				data: JSON.stringify({"title": "naturalije",
									  "email": $('#naturalijeemail').val(),
									  "body": $('#naturalijetextarea').val()}),
				dataType: "json",
				success: function(data) {
					console.log(data);
					startConfetti();
					$('#naturalijepopup').removeClass('open');
				},
			});
		} else {
			$('.naturalijeform').shake();
		}
	});

	$('.btn-finish-majica').on('click', function() {

		if ($(this).parent().parent().children('.artikeltogglecontainer:nth-of-type(1)').children('.artikeltoggle').hasClass('dolzniselected') && $(this).parent().parent().children('.artikeltogglecontainer:nth-of-type(2)').children('.artikeltoggle').hasClass('dolzniselected')) {
			// everything OK

			// add to cart
			// determine what it's for
			if ($(this).parents('.popup').attr('id') === 'majicapopup') {
				// majica

				// generate data
				var name = 'majica';
				if ($(this).parent().siblings('.majicatype').children('.dolzniselected').text() === 'ohlapen') {
					name = name + 'oh' + $(this).parent().siblings('.majicasize').children('.dolzniselected').text();
				} else {
					name = name + 'op' + $(this).parent().siblings('.majicasize').children('.dolzniselected').text();
				}
				var quantity = $(this).parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
				var details = {
					'realname': 'Majica',
					'type': $(this).parent().siblings('.majicatype').children('.dolzniselected').text(),
					'size': $(this).parent().siblings('.majicasize').children('.dolzniselected').text()
				}

				// ga za majico step2
				ga('send', {
					'hitType': 'event',
					'eventCategory': 'majica',
					'eventAction': 'step2',
					'eventLabel': name
				});

			} else {
				alert('rizle');
				// ker ni drugega morajo bit rizle
				// generate data
				var name = 'rizle'
				var quantity = $(this).parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
				var details = {}

			}
		} else {
			$(this).parent().parent().children('.artikeltogglecontainer, .artikellable').not('.noshake').shake();
		}
	});

	$('.btn-finish-rizle').on('click', function() {

		// ker ni drugega morajo bit rizle
		// generate data
		var name = 'rizle'
		var quantity = $(this).parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
		var details = {}

		// ga za rizle step2
		ga('send', {
			'hitType': 'event',
			'eventCategory': 'rizle',
			'eventAction': 'step2',
			'eventLabel': 'rizle' + quantity
		});
	});

	$('.btn-finish-salca').on('click', function() {

		// ker ni drugega mora bit salca
		// generate data
		var name = 'salca'
		var quantity = $(this).parent().siblings('.artikeltogglecontainer').children('.artikelcounter').children('.artikelnumber').text();
		var details = {}

		// ga za salca step2
		ga('send', {
			'hitType': 'event',
			'eventCategory': 'salca',
			'eventAction': 'step2',
			'eventLabel': 'salca' + quantity
		});

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

		if ($(this).text() == '"moški"') {
			$(all_shirts.diff(shirts["m"]).join(", ")).addClass('hidden');
			$(shirts["m"].join(", ")).removeClass('hidden');

		} else if ($(this).text() == '"ženski"') {
			$(all_shirts.diff(shirts["z"]).join(", ")).addClass('hidden');
			$(shirts["z"].join(", ")).removeClass('hidden');
		}

		// activate button

		// prevent shaking
		$(this).parent().addClass('noshake').prev().addClass('noshake');
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

			// ga za enkratno donacijo
			ga('send', {
				'hitType': 'event',
				'eventCategory': 'one_time_d',
				'eventAction': 'step2'
			});

			// all OK
			if ($(this).prev().children('.selected').hasClass('velikosrceinput')) {
				selectDonation(parseInt($(this).prev().children('.selected').children('.input-drugo').val()), false)
			} else {
				var amount = $(this).prev().children('.selected').text().split(' ')[$(this).prev().children('.selected').text().split(' ').length - 2]
				console.log(amount);
				selectDonation(parseInt(amount), false);
			}

			window.open('./donacija', '_blank');
			$('.popup.open').removeClass('open');
		}
	});

	$('#submitredna').on('click', function() {
		if (!$(this).siblings('.velikosrcetilecontainer').children().hasClass('selected')) {
			$(this).prev().shake();
		} else {
			// all OK

			// ga za redno donacijo
			ga('send', {
				'hitType': 'event',
				'eventCategory': 'regular_d',
				'eventAction': 'step2'
			});

			if ($(this).prev().children('.selected').hasClass('velikosrceinput')) {
				selectDonation(parseInt($(this).prev().children('.selected').children('.input-drugo').val()), true)
			} else {
				var amount = $(this).prev().children('.selected').text().split(' ')[$(this).prev().children('.selected').text().split(' ').length - 2]
				selectDonation(parseInt(amount), true);
			}

			window.open('donacija#redna', '_blank');
			$('.popup.open').removeClass('open');
		}
	});

	// shaker, ga and close popup
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

				// ga za majico step3
				ga('send', {
					'hitType': 'event',
					'eventCategory': 'majica',
					'eventAction': 'step3',
					'eventLabel': name
				});

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

			// ga za rizle step3
			ga('send', {
				'hitType': 'event',
				'eventCategory': 'rizle',
				'eventAction': 'step3',
				'eventLabel': 'rizle' + quantity
			});

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


	// zaključi nakup
	$('.btn-zakljuci, .btn-vozicek-zakljuci').on('click', function() {
		document.location.href='/dolzni/vozicek'
	});

});
