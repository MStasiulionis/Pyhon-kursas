//antra uzduotis
const budgets = [
  {
    name: "Rytis",
    budget: 50,
  },
  {
    name: "Saulė",
    budget: 230,
  },
  {
    name: "Paulius",
    budget: 1500,
  },
  {
    name: "Gytis",
    budget: 92,
  },
  {
    name: "Sandra",
    budget: 7,
  },
];

const names = budgets.map((person) => person.name);
console.log(names);

function isPersonInArray(names, whatName) {
    if (names.includes(whatName) == true) {
        if (whatName.endsWith("a") || whatName.endsWith("ė")){
            console.log("Welcome Miss. "+whatName);
        } else
        console.log("Welcome Mr. "+whatName);
    } else
    console.log("Unfortunately Name is not in our list.")
}
isPersonInArray(names, 'Mykolas')

let numbersArr = [2,2,1,2,5,1,4,66,2,2,3,6,2]

function arrCountTwos(numbersArr){
    let arr = numbersArr.filter(x => x=2)
    return arr.length
}
console.log(arrCountTwos(numbersArr))