var enkratnaHTML = [    '<div class="pregleditemcontainer">',
                    '<div class="pregleditemimage" style="background-image: url(../../img/donacija.png);" data-img="../../img/donacija.png"></div>',
                    '<p class="pregleditemdescription"> Enkratna donacija</p>',
                    '<p class="pregleditemprice">{{ itemquantity }} x {{ itemprice }} €</p>',
                    '</div>'].join('\n');
var rednaHTML = [   '<div class="pregleditemcontainer">',
                    '<div class="pregleditemimage" style="background-image: url(../../img/donacija.png);" data-img="../../img/donacija.png"></div>',
                    '<p class="pregleditemdescription"> Redna donacija</p>',
                    '<p class="pregleditemprice">{{ itemquantity }} x {{ itemprice }} €</p>',
                    '</div>'].join('\n');

var d = new Date();


function renderEnkratna(itemprice, itemquantity) {
    return enkratnaHTML.replace('{{ itemprice }}', itemprice).replace('{{ itemquantity }}', itemquantity);
}

function renderRedna(itemprice, itemquantity) {
    return rednaHTML.replace('{{ itemprice }}', itemprice).replace('{{ itemquantity }}', itemquantity);
}

function calculatePrice() {
    var price = 0;

    $.each(basket_items, function(i, e) {
        price = price + (parseInt(e['article']['price']) * parseInt(e['quantity']));
    });

    $('.paypalprice').val(price);

    return price;
}

function renderSummary(isSubscription) {
    // dodaj artikle

    $.each(basket_items, function(i, e) {
        if (e['article']['name'].indexOf('donacija') !== -1) {
            if (isSubscription) {
                // redna je
                $('.pregledtotal').before(renderRedna(e['quantity'], 1));
            } else {
                // enkratna je
                $('.pregledtotal').before(renderEnkratna(e['quantity'], 1));
            }
        }
    });

    $('.pregledtotalprice').text(calculatePrice() + ' €');
}


var allgood = false;
var payment = false;
var costumer_data = {}

var shopObject = {
    'id': $.cookie('djndid'),
    'name': '',
    'details': '',
    'payed': 'false',
    'payment_type': '',
    'delivery': '',
    'address': ''
}
var basket_items = []
$(document).ready(function() {

    if (window.location.href.indexOf('hvala') !== -1) {
        $('.card-vozicek').addClass('hidden');
        $('.vozicek-hvala').removeClass('hidden');
    }


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

            costumer_data['name'] = $('#donacijanamelastname').val()
            costumer_data['email'] = $('.emailshopinput').val()
            costumer_data['info'] = $('#narocniknotform textarea').val()
            costumer_data['phone'] = ''
            costumer_data['address'] = ''
            costumer_data['delivery_method'] = ''



            $(this)
                .parent()
                .addClass('hidden')
                .next()
                    .removeClass('hidden');
            $('.vozicekstep.active')
                .removeClass('active')
                .next()
                    .addClass('active');

            if (basket_items[0]["article"]["name"].indexOf('Enkratna') !== -1) {
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

        // NEW CHECKOUT
    $('.btn-placaj').on('click', function() {
        kuki = JSON.parse($.cookie()["donation"])
        key = kuki["key"];
        isSubscription = kuki["isSubscription"];

        var poloznica = $('input:radio[id="placajspoloznico"]:checked').val() === 'on';
		var paypal = $('input:radio[id="placajspaypalom"]:checked').val() === 'on';
		var $this = $(this);

		if (poloznica || paypal) {
			$this.attr('disabled', true);
			$this.append('<div class="lds-dual-ring" style="margin-left:20px"></div>');
		}

        // UPN
        if(poloznica){
            costumer_data["payment_type"] = "upn"
            $.ajax({
                type: "POST",
                url: "https://shop.djnd.si/api/checkout/?order_key=" + key,
                data: JSON.stringify(costumer_data),
                dataType: "json",
                success: function(data) {
                    console.log('sem poslu checkout');
                    console.log(data);
                    $.ajax({
                        type: "POST",
                        url: "https://shop.djnd.si/poloznica/",
                        data: JSON.stringify(data),
                        dataType: "html",
                        success: function(data) {
                            console.log('dobu sem poloznco');
                            console.log(data);
                            $(".vozicekhtml").html(data);
                            $.removeCookie('basket', {"path": "/"});
                        },
                    });
                    $.removeCookie('donation', {"path": "/"});
                }
            });
        }
        // PAYPAL
        else if (paypal) {
            costumer_data["payment_type"] = "paypal";
            costumer_data["subscription"] = isSubscription;
            costumer_data["success_url"] = "https://danesjenovdan.si/dolzni/?success=true";
            costumer_data["fail_url"] = "https://danesjenovdan.si/dolzni/?success=false&donacija=true";
            console.log(costumer_data)
            $.ajax({
                type: "POST",
                url: "https://shop.djnd.si/api/checkout/?order_key=" + key,
                data: JSON.stringify(costumer_data),
                dataType: "json",
                success: function(data) {
                    console.log(data);
                    $.removeCookie('donation', {"path": "/"});
                    window.location.replace(data["redirect_url"])
                }
            });
        }

    });
    var donation = JSON.parse($.cookie()["donation"])
    function getBasketItems(key){
        $.get("https://shop.djnd.si/api/items/?order_key=" + donation["key"], function(data) {
            basket_items = data;
            renderSummary(donation.isSubscription)
            $(".overlay, .lds-heart").hide();
        });
    }
    getBasketItems(donation["key"])

});
