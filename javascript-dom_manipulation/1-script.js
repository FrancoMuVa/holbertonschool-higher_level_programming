document.addEventListener('DOMContentLoaded', function () {
    var red_header = document.getElementById("red_header");
    var header = document.body.querySelector("header");
    red_header.addEventListener('click', function () {
        header.style.color = '#FF0000';
    });
})
