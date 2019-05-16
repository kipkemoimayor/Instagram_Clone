//js here
$(document).ready(function() {
  $("#change").click(function(){
    $("#card").addClass("bg-color")
    $("#side").show()
    $("#side").animate({
      transition:"500ms",
      right:"250px",
      left:"0"
    })
  })

});
