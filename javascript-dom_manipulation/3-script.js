document.addEventListener('DOMContentLoaded', function () {
    var toggle_header = document.getElementById("toggle_header");
    var header = document.body.querySelector("header");
    toggle_header.addEventListener('click', function () {
        header.classList.toggle('red');
        header.classList.toggle('green');
    });
})
