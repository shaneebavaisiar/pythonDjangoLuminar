// find min value from array and total of array

arr=[4,39,20,,3,47,12,7,9]
var total=arr.reduce((num1,num2)=>num1+num2)
console.log(total)

var min=arr.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(`min value is ${min}`)