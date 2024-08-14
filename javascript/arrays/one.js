const fruits = []
fruits.push('mango', 'orange', 'banana', 'apple');
console.log(fruits);
console.log(fruits.length);

fruits[6] = 'lemon';
console.log(fruits[6]);
console.log(fruits.length);

fruits.length = 10;
console.log(fruits)
console.log(fruits[8]);

fruits.length = 3;
console.log(fruits.length);
console.log(fruits)
console.log(Object.keys(fruits));

