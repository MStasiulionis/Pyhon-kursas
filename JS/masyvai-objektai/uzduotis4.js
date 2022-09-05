const arr = ['I', 'study', 'JavaScript', 'right', 'now'];

arr.splice(0, 3, "Let's", "dance")
let string = arr.join(" ")

let first = ['slice', 'splice', 'concat'];
let second = ['push', 'pop', 'shift', 'unshift'];
let newArr = first.concat(second, "length", 7, {subject:'methods'})
console.log(newArr)

let accords = ["D", "G", "C", "C7", "F"];

function checkAccords () {
    for (let i = 0; i < accords.length; i++) {
    if (accords[i].endsWith("7")){
    continue
    }else{
    changeAccords(accords[i])
    }

    }
}

function changeAccords(value){

}