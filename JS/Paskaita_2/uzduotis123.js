const car = 'Audi';
const bmwGroup = ['BMW', 'Mini', 'Rolls-Royce'];
const vwGroup = ['VW', 'Audi', 'Bentley', 'Bugatti', 'Lamborghini', 'Porsche'];

switch(car)  {
    case "BMW":
    case "Mini":
    case "Rolls-Royce":
    console.log('Your car is in BMW Group');
    break;
    case "VW":
    case "Audi":
    case "Bentley":
    case "Bugatti":
    case "Lamborghini":
    case "Porsche":
    console.log('Your car is in VW Group');
    break;
    default:
    console.log('Your car dont belong to any group')
}
let userInput = 'Obuolys';

switch(userInput) {
    case "Slyva":
    case "Obuolys":
    case "Bananas":
    case "Kriaušė":
    case "Apelsinas":
    console.log('Vaisius');
    break;
    case "Bulvė":
    case "Agurkas":
    case "Svogūnas":
    case "Česnakas":
    case "Baklažanas":
    console.log('Daržovė');
    break;
    default:
    console.log('Not in the list!')
}