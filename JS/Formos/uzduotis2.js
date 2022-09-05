//1.
//function raideL(event) {
//    const size = event.target.value
//    let output = ''
//    for (i = 0; i < size - 1; i++) {
//       output += 'L<br>';
//    }
//    let a = size - 1
//    for (i = 0; i < size; i++) {
//       output += 'L'
//    }
//    document.querySelector('p').innerHTML = output;
//}
//document.querySelector('input').addEventListener('input', raideL)
//2.
//function raideC(event) {
//    const size = event.target.value
//    let output = ''
//    for (i = 0; i < size-1; i++) {
//       output += 'C'
//    }
//    for (i = 0; i < size - 1; i++) {
//       output += 'C<br>';
//    }
//    for (i = 0; i < size; i++) {
//       output += 'C'
//    }
//    document.querySelector('p').innerHTML = output;
//}
//document.querySelector('input').addEventListener('input', raideC)
//3.
//function addNameToList(event) {
//     const name = event.target.value.trim();
//     const outputElement = document.getElementById('output');
//     if (name) {
//       outputElement.innerText += `${name}, `;
//     }
//   }
//document.getElementById('name').addEventListener('blur', addNameToList);
//4.
//function alertNearestNumber(n1, n2) {
//     if (Math.abs(100 - n1) > Math.abs(100 - n2)) {
//       alert(n2);
//     }
//     else {
//       alert(n1);
//     }
//   }
//
//   function handleFormSubmit(event) {
//     event.preventDefault();
//     const n1 = Number(document.getElementById('number1').value);
//     const n2 = Number(document.getElementById('number2').value);
//     alertNearestNumber(n1, n2);
//   }
//
//   document.querySelector('form').addEventListener('submit', handleFormSubmit);
//5.
// let randomNumber = Math.floor(Math.random() * 5) + 1;
// console.log(randomNumber);
//
// function guessNumber(event) {
//   event.preventDefault();
//   const guessedNumber = Number(document.getElementById('guess').value);
//   if (randomNumber === guessedNumber) {
//     alert("Atspėjai, numeris buvo " + randomNumber)
//   }
//   else {
//     alert("Neatspėjai, numeris buvo " + randomNumber)
//   }
// }
//
// document.querySelector('form').addEventListener('submit', guessNumber);
//6.
let counter = 0;
let randomNumber = Math.floor(Math.random() * 5) + 1;
console.log(randomNumber);

function guessNumber(event) {
   event.preventDefault();
   counter++;
   const guessedNumber = Number(document.getElementById('guess').value);
   if (randomNumber === guessedNumber) {
     alert(`Atspėjai iš ${counter} karto`);
   }
   else {
     alert("Neatspėjai");
   }
}

document.querySelector('form').addEventListener('submit', guessNumber);

