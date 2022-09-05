let numbers = [5, 1, 7, 2, -9, 8, 2, 7, 9, 4, -5, 2, -6, 8, -4, 6];

numbers.forEach(printHtml)
function printHtml (v, i) {
    const element = document.querySelector("body");
    const para = document.createElement('p');
    element.appendChild(para);
    element.lastElementChild.innerHTML = 'index nr:'+i +'value: '+ v
}
