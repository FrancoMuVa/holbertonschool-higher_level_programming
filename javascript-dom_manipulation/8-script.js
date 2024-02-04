document.addEventListener('DOMContentLoaded', function () {
    var hello = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            const salutElem = document.createTextNode(data.hello);
            hello.appendChild(salutElem);
        })
});
