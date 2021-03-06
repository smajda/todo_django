
var show = '12%';
var hide = '3%';
var nav_expanded = false;
$("#nav").css('width', show)
$("#content").css('margin-left', show);

$("#nav_toggle").click(function () {
  var nav = $("#nav");
  var content = $("#content");
  var nav_icon = $(".nav_icon");
  var nav_toggle = $("#nav_toggle");
  if (nav_expanded) {
    nav.css('width', show)
    content.css('margin-left', show);
    nav_icon.css('padding', '10%');
    nav_toggle.toggleClass( "mirror_img" );
    nav_expanded = false;
  } else {
    nav.css('width', hide)
    content.css('margin-left', hide);
    nav_icon.css('padding', '10%');
    nav_toggle.toggleClass( "mirror_img" );
    nav_expanded = true;
  }
});
