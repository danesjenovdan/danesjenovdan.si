$(document).ready(function () {
    if ($('.subheader').height() < $(window).height() - 64) {
        $('.subheader').height($(window).height() - 64);
    }
    $(window).on('resize', function () {
        if ($('.subheader').height() < $(window).height()) {
            $('.subheader').height($(window).height() - 64);
        }
    });

    $('.kazalolink').on('click', function (event) {
        event.preventDefault();
        $('#therealobcasnik, #therealobcasnik > body').animate({
            scrollTop: $('#kazalo-' + $(this).data('order')).offset().top - 100
        });
    });

    $('.takemeup').on('click', function(event) {
        event.preventDefault();
        $('#therealobcasnik, #therealobcasnik > body').animate({
            scrollTop: 0
        });
    });
});