const person = {
name: "Rosa", age: 120, alive: false,
interests: ["swimming", "cards"]
};

person.name = 'Rosalina'
person.age = Math.round(Math.random() * 120);
if (person.age < 100) {
    person.alive = !person.alive;
    person.interests.push('enjoying life')
}

console.log(person)