var clk=document.querySelector('#clk')

clk.addEventListener('click',()=>{
    clk.textContent='clicked';
    clk.style.color='red';
})


var dbl=document.querySelector('#dbl')
dbl.addEventListener('dblclick',()=>{
    dbl.textContent='double clicked';
    dbl.style.color='green';
})


var over=document.querySelector('#over')
over.addEventListener('mouseover',()=>{
    over.textContent='mouse over me';
    over.style.color='orange'

})
var over=document.querySelector('#over')
over.addEventListener('mouseout',()=>{
    over.textContent='mouse not over me';
    over.style.color='red'

})