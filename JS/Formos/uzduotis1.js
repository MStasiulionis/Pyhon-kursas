document.querySelector("form").addEventListener("submit", myFunction);

//function myFunction(event) {
//    event.preventDefault();
//    const clientAge = event.target.elements.age.value;
//    if (clientAge <= 16) {
//        document.querySelector("h1").innerHTML = "3eur"
//    } else if (clientAge >= 60){
//         document.querySelector("h1").innerHTML = "3,60eur"
//    } else {document.querySelector("h1").innerHTML = 6+"eur"}
//}

function myFunction(event) {
    event.preventDefault();
    const clientAge = event.target.elements.age.value;
    const criminalRecord = event.target.elements.criminal.checked;
    if (clientAge < 18 || clientAge > 30) {
        document.querySelector("h1").innerHTML = "Eiti į armiją nereikia!"
    } else if (criminalRecord === false){
         document.querySelector("h1").innerHTML = "Eiti į armiją reikia!"
    } else {document.querySelector("h1").innerHTML = "Eiti į armiją nereikia!"}
}