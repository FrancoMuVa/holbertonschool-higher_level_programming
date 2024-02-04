document.addEventListener('DOMContentLoaded', function () {
    var character = document.getElementById("character");
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then((res) => {
            return res.json()
        })
        .then((data) => {
           const name = document.createTextNode(data.name);
           character.appendChild(name);
        })
});
