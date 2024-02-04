document.addEventListener('DOMContentLoaded', function () {
    var update_header = document.getElementById("update_header");
    var header = document.body.querySelector("header");
    update_header.addEventListener('click', function () {
        const newText = document.createTextNode('New Header!!!');
        header.innerHTML = '';
        header.appendChild(newText);
    });
})
