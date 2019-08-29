// NAVBAR SCRIPT
$(function() {
  $(document).scroll(function() {
    var $navbar = $("#mainNavbar");
    $navbar.toggleClass("scrolled", $(this).scrollTop() > $navbar.height()); // css transition effect
    $navbar.toggleClass(
      "navbar-darkmode",
      $(this).scrollTop() > $navbar.height()
    ); //Background
  });
});
