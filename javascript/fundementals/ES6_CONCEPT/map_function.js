// print all squres of number


arr=[1,2,3,4]

var squres=arr.map(num=>num**2)
console.log(squres)

// or
arr.map(num=>num**2).forEach(num => {
    console.log(num)
    
});