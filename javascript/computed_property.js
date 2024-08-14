const key = 'name';
const person = {
  [key]: 'Micheal'
};

console.log(person);

const getKey = () => 'age';
const person2 = {
  [getKey()]: 40
}

console.log(person2);
