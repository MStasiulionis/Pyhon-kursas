let name = 'Mykolas';

const nameLength = name.length < 5 ? 'Short name!' : 'Long name!';
console.log(nameLength);

let userAge = 21;
let legalAge = 20;

const canDrive = userAge < 0 || userAge > 120 ? 'Invalid age' : userAge >= legalAge ? 'User can drive!' : 'User cant drive!';
console.log(canDrive)