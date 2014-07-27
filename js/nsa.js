function updateVictim(id, name, lastname, email, fbid) {
	$.post('http://djapi.danesjenovdan.si/nsa/updatevictim', {
		'id': id,
		'name': name,
		'lastname': lastname,
		'email': email,
		'fbid': fbid
	}, function(r) {
		console.log(r);
	});
}

function checkVictim(id) {
    $.post('http://djapi.danesjenovdan.si/nsa/checkvictim', {
		'id': id
	}, function(r) {
		if (r != 1) {
            $.removeCookie('djndid', {path: '/'});
            $.removeCookie('dolzniCart', {path: '/'});
            $.removeCookie('djndconsent', {path: '/'});
            
            $.post('http://djapi.danesjenovdan.si/nsa/createanonvictim', function(r) {
                $.cookie('djndid', r, { 'expires': 730, 'path': '/'});
            });
        }
	});
}

function getCurrentID() {
    return $.cookie('djndid');
}

function getConsent() {
    if ($.cookie('djndconsent')) {
        return $.cookie('djndconsent');
    }
    
    return false;
}

function updateConsent() {
    if (getConsent() != 1) {
        $.cookie('djndconsent', 1, {'expires': 730, 'path': '/'});
    }
}

$(document).ready(function() {
    // check for broken victim
    checkVictim($.cookie('djndid'));
    
	// check for cookie
	if ($.cookie('djndid')) {
		// old acquaintance
		// hide the warning
        if (getConsent() == 1) {
            $('.cookiewarning').css('display', 'none');
        }
		
	} else {
		// first time user
		$.post('http://djapi.danesjenovdan.si/nsa/createanonvictim', function(r) {
			$.cookie('djndid', r, { 'expires': 730, 'path': '/'});
		});
	}
    
});


// EXAMPLE USE
//    // agree with cookies
//    $('.confirmcookies').on('click', function() {
//        updateConsent();
//    });
//    // get more info about cookies
//    $('.cookiemoreinfo').on('click', function() {
//        window.open('http://danesjenovdan.si/piskotki/', '_blank');
//    });