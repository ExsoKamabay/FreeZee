
  function openNav() {
    $("#mySidenav").css({
      "width" : "230px",
      "border-top-right-radius":"50px",
      "border-right":"3px solid green",
      });
    openNav.animate()
    }
  function closeNav() {
      $("#mySidenav").css({
        "width":"0px",
        "border":"none",
      });
    }