$(document).ready(function () {
$('.carosel-control-right').click(function() {
  $(this).blur();
  $(this).parent().find('.carosel-item').first().insertAfter($(this).parent().find('.carosel-item').last());
});
$('.carosel-control-left').click(function() {
  $(this).blur();
  $(this).parent().find('.carosel-item').last().insertBefore($(this).parent().find('.carosel-item').first());
});


$('.itDescBtn').click(function () {
$('#desc').toggle();

    });

$(window).scroll(function() {
    if($(window).scrollTop() == $(document).height() - $(window).height()) {
        appendData();
    }
});
function appendData() {
     var orginal = $('#sI');
     orginal.clone().css({}).appendTo('#sPace');
        }
$('#cartBtn').click(function () {
    $( "#dialog" ).dialog();
  });

});
