//---------Problem 1---------
let bdays = ['10-17', '05-19', '20-19'];
let newBdays = bdays.map(function(elem1) { 
    return elem1.replace('-','/');
});

console.log(newBdays);

//--------Problem 2----------
let value = [1,2,3,4,5,6];
let newValue = value.map(function(elem2) {
    return elem2*2
});

console.log(newValue);

//--------Problem 3----------
let arr = [1.5, 2.56, 5.1, 12.33];
let rounded = arr.map(Math.ceil);

console.log(rounded);

//--------Problem 4----------
let nums = [1,2,3,4];
let sum = nums.reduce(function(prevVal1, curVal1) {
    return prevVal1 + curVal1
});

console.log(sum);

//-------Problem 5-------------
var filterValue = [-4,3,2,-21,1];
var pos = filterValue.filter(function(el) {
    return el > 0
});

console.log(pos);

//-------Problem 6-------------
var data = [ 
    {name:'daniel', age:45},
    {name: 'john', age:30},
    {name:'robert', age:null},
    {name:'jen', age:undefined},
    {name: null, age:undefined}
];

var dataMod = data.filter(function(el1) { 
    return el1['age']  !== undefined
});

console.log(dataMod);