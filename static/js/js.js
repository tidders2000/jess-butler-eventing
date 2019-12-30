$(document).ready(function() {
    $('.slider').slider({ full_width: true, indicators: false, height:800 });
    $(".button-collapse").sideNav();
    $('.modal').modal();

    $('.image_container').on('mouseover', function(event) {
        $(this).find('p').fadeOut();
    });

    $('.image_container').on('mouseout', function(event) {
        $(this).find('p').stop().fadeIn();
    });

    $(window).scroll(function() {
        if ($(this).scrollTop() > 0) {
            $('.fadeslider').fadeOut();
        }
    });
});
