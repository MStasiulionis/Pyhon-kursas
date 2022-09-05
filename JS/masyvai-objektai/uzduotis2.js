let myObject = {name: 'Jonas', toysArray:['Cars', 'Robot', 'Plane'], yearsOld: 10, birthday: true, totalToys:null,
                friends:[{name: 'Tom', doing:'Playing with his toy'}, {name: 'Steve', doing: 'Sleeping'}, {name: 'Ben',
                doing:'Playing with friends'}]}

function birthdayActivity () {
    if (myObject.birthday) {
        myObject.toysArray.shift();
        myObject.toysArray.push('Xbox');
        myObject.yearsOld = myObject.yearsOld + 1;
        myObject.totalToys = myObject.toysArray.length
        for (let i=0; i < myObject.friends.length; i++)
            console.log(myObject.friends[i].name, myObject.friends[i].doing)
    } else
    console.log("It's not your birthday")

}
birthdayActivity()