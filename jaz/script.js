$(document).ready(function() {
    if (document.location.href.indexOf('token') === -1) {
        $('.logged-out').css('display', 'block');
        $('.logged-in').css('display', 'none');
    }

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

    $('.switch input[type="checkbox"]').on('change', function() {
        var target = $(this).parent().data('target');
        
        // call API here
        url = 'http://localhost:8000/confirm-' + target + '/?token=' + paramObject.token + '&email=' + paramObject.email + '&permission=' + this.checked;
        console.log(url);
        $.get(url, function(r) {
            console.log(r);
            if (r !== '1') {
                alert(r);
            }
        });
        
    });
});