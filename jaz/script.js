$(document).ready(function() {
    var paramObject = {};
    window.location.search
        .slice(1)
        .split('&')
        .filter(function(val) {
            return val;
        })
        .forEach(function(val) {
            var s = val.split('=');
            paramObject[s[0]] = s[1];
        });

    if (!paramObject.token || !paramObject.email) {
        $('.logged-out').css('display', 'block');
        $('.logged-in').css('display', 'none');

        ga('send', {
            'hitType': 'event',
            'eventCategory': 'gdpr',
            'eventAction': 'landing-logged-out'
        });

        $('#submitemailform').on('submit', function(event) {
            event.preventDefault();
            var email = $('#gdpremail').val();
            if (email) {
                $.get('https://spam.djnd.si/deliver-email/?email=' + email, function(r) {
                    if (r === '1') {
                        ga('send', {
                            'hitType': 'event',
                            'eventCategory': 'gdpr',
                            'eventAction': 'deliver-email'
                        });
                        alert('Sporočilo poslano na e-naslov!');
                    } else {
                        ga('send', {
                            'hitType': 'event',
                            'eventCategory': 'gdpr',
                            'eventAction': 'deliver-email-error'
                        });
                        alert('Prišlo je do napake :(');
                    }
                });
            } else {
                alert('Prosim vpiši e-naslov.');
            }
        });
    } else {
        ga('send', {
            'hitType': 'event',
            'eventCategory': 'gdpr',
            'eventAction': 'landing-logged-in'
        });

        $('#save-button').on('click', function(event) {
            event.preventDefault();
            alert('Shranjeno!');
        });

        $('#person').text(paramObject.email);

        $.get('https://spam.djnd.si/get-settings/?token=' + paramObject.token + '&email=' + paramObject.email, function(r) {
            if (r === 'Ne goljufaj prosim.') {
                document.location.href = './';
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
            var checked = this.checked;
            var label = $(this).parent().parent().parent().find('.toggle-label');

            if (checked) {
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
                    label.text(checked ? 'Naročeno!' : 'Naročite me!');
                    ga('send', {
                        'hitType': 'event',
                        'eventCategory': 'gdpr',
                        'eventAction': target + '-' + checked
                    });
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
                        ga('send', {
                            'hitType': 'event',
                            'eventCategory': 'gdpr',
                            'eventAction': target + '-' + checked
                        });
                    }
                });
            }
        });
    }
});
