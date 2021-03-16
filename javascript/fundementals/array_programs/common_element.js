var arr1=[10,20,30,40,51]
var arr2=[21,22,30,31,40,41]

var i=0
var j=0
while(i<=arr1.length){
    while(j<=arr2.length){
        if (arr1[i]==arr2[j]){
            console.log(arr1[i])
            i++
            j++
            break
        }
        else if(arr1[i]<arr2[j]){
            i++
            break

        }
        else{
            j++
            

        }
        
    }
    
}