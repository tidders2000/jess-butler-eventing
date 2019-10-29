$(document).ready(function() {
    $('.slider').slider({ full_width: true });
    $(".button-collapse").sideNav();
    $('.modal').modal();

    $(window).scroll(function() {
        if ($(this).scrollTop() > 0) {
            $('.slider').fadeOut();
        }
    });
});
