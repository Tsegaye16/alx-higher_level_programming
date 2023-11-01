"use strict"
$("DIV#toggle_header").click(function(){
    $("header").hasClass("red") ? $("header").removeClass("red").addClass("green") : $("header").removeClass("green").addClass("red")
})
