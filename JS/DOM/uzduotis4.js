//1.
//const h1 = document.querySelector("h1")
//document.addEventListener("click", (event) => {
//    event.target.style.fontSize = "48px";
//    event.target.style.textAlign = "center";
//    event.target.style.color = "red";} )
//2.
//const button = document.querySelector('button');
// button.style.cssText = 'position:absolute; top:0; left:0;';

// let isInOriginalPosition = true;
// function changeLoc() {
//   event.target.style.cssText = isInOriginalPosition ? 'position:absolute; bottom:0; right:0;' : 'position:absolute; top:0; left:0;';
//   isInOriginalPosition = !isInOriginalPosition;
// }
//3.
//let topLeft = true
//let topRight = false
//let bottomRight = false
//let bottomLeft = false
//function changeLoc() {
//    if (topLeft) {
//       event.target.style.cssText = 'position:absolute; top:0; right:0;'
//       topLeft = !topLeft
//       topRight = !topRight
//    } else if (topRight) {
//        event.target.style.cssText = 'position:absolute; bottom:0; right:0;'
//        topRight = !topRight
//        bottomRight = !bottomRight
//    } else if (bottomRight) {
//        event.target.style.cssText = 'position:absolute; bottom:0; left:0;'
//        bottomRight = !bottomRight
//        bottomLeft =!bottomLeft
//    } else {
//        event.target.style.cssText = 'position:absolute; top:0; left:0;'
//        bottomLeft =!bottomLeft
//        topLeft = !topLeft
//    }
//}
//4.
//document.getElementById('name').addEventListener('input', changeColor);
//function changeColor(event) {
//    const name = event.target.value
//    console.log(name)
//    document.body.style.backgroundColor = name.length < 3 ? 'red' : 'green'
//}
//5.
//const colors = ["red", "green", "blue", "yellow"]
//function changeLoc(){
//    const randomIndex = Math.round(Math.random() * 4);
//    event.target.style.backgroundColor = colors[randomIndex];
//}
//6.
//function changeLoc(){
//    const randomR = Math.round(Math.random() * 255);
//    const randomG = Math.round(Math.random() * 255);
//    const randomB = Math.round(Math.random() * 255);
//    event.target.style.backgroundColor = "rgb(" + randomR + "," + randomG + "," + randomB + ")";
//}