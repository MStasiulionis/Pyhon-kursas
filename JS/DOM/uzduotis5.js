//document.querySelector(".change-text").innerHTML = "<h1>Čia tekstas parašytas su JS</h1>"

const para = document.createElement("h1");
const node = document.createTextNode("Mykolas");
para.appendChild(node);
const element = document.querySelector("body");
element.appendChild(para);
document.querySelector("h1").style.color = 'red';



const list = document.createElement('ul')
element.appendChild(list)
const brands = ['Audi', 'BMW', 'VW']
for (let i = 0; i < brands.length; i++) {
    console.log(i);
    console.log(brands[i])
    document.createElement('li')
    let item = document.querySelector("li").innerHTML = brands[i];
    element.appendChild(item)
    }




