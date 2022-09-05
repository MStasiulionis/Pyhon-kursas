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
const monies = budgets.map((person) => person.budget);
const monies2 = [250,500,300,480,1250]

console.log(monies.some(x => x < 0))

function belowHundred (arr) {
    if (arr.some(x => x < 100) == true){
        return arr.filter(x => x > 100)
    } else {
        console.log("All numbers are above 100")
    }
}
console.log(belowHundred(monies2))

function simbolified (arr) {
    if (arr.some(x => x.length > 3) == true){
        for (let i = 0; i < arr.length; i++) {
            symbolArr = arr[i].split("");
            if (symbolArr.includes("a") == true){
                arr[i].replace()
            let newArr = }
        }
    }
}