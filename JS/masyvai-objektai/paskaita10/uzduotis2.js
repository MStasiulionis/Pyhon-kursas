let numbers = [5, 1, 7, 2, -9, 8, 2, 7, 9, 4, -5, 2, -6, 8, -4, 6];

let newNumbers = numbers.map(arrDouble);
let newNumbers1 = numbers.map(arrMultiple, {arg: 5});
//let newNumbers = numbers.map(x => x*2)

function arrDouble(element) {
    return element * 2
}
function arrMultiple(element) {
    return element * this.arg
}