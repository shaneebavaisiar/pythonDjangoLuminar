function display(num) {
    var res=document.querySelector('.text')
    res.value+=num
    
}
function printAnswer() {
    var res=document.querySelector('.text').value;
    var out=eval(res)
    document.querySelector('.text').value=out;
   
}

function del() {
    var res=document.querySelector('.text').value;
    var data=res.slice(0,-1)
    document.querySelector('.text').value=data
    
}
function clr() {
    var res=document.querySelector('.text').value;
    var data=res.substr(0,0)
    document.querySelector('.text').value=data
    
}