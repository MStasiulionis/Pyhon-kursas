document.querySelector("form").addEventListener("submit", saveCookie);

let cookie = document.cookie.match(color).input
document.body.style.backgroundColor = cookie.split("=")[1]


function saveCookie(event) {
    let colorId = event.target.elements.color.value
    document.cookie = 'color=' + colorId;
    alert(document.cookie)
    document.body.style.backgroundColor = colorId
}

function deleteCookie() {
    document.cookie = 'color=' + cookie.split("=")[1] + '; max-age=-1';
}
