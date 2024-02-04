document.addEventListener('DOMContentLoaded', function () {
    var add_item = document.getElementById("add_item");
    var my_list = document.body.querySelector(".my_list");
    add_item.addEventListener('click', function () {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode("Item"));
        my_list.appendChild(li);
    });
})
