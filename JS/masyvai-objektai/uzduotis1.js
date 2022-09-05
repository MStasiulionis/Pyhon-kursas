let myArray = []

function shiftFunc() {
    let arrayElement = document.getElementsByTagName('input')[0].value
    myArray.shift()
    console.log(myArray)
    document.getElementsByTagName('p')[0].innerHTML = myArray
}

function popFunc() {
    let arrayElement = document.getElementsByTagName('input')[0].value
    myArray.pop()
    console.log(myArray)
    document.getElementsByTagName('p')[0].innerHTML = myArray
}
function unshiftFunc() {
    let arrayElement = document.getElementsByTagName('input')[0].value
    myArray.unshift(arrayElement)
    console.log(myArray)
    document.getElementsByTagName('p')[0].innerHTML = myArray
}

function pushFunc() {
    let arrayElement = document.getElementsByTagName('input')[0].value
    myArray.push(arrayElement)
    console.log(myArray)
    document.getElementById('show').innerHTML = myArray
}