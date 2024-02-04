document.addEventListener('DOMContentLoaded', function () {
    var list_movies = document.getElementById("list_movies");
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then((res) => {
            return res.json()
        })
        .then((data) => {
            const dataArray = data.results;
            for (let movie of dataArray) {
                var li = document.createElement('li')
                li.appendChild(document.createTextNode(movie.title));
                list_movies.appendChild(li)
            }
        })
});
