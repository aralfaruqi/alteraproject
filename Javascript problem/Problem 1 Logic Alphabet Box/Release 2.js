function generateAlphabetBoard() {
  const hasilAlphabet = [];
  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  for (let i=0; i<=8; i++) {
    let barisAlphabet = [];
    for (let j=0; j<=8; j++) {
      barisAlphabet.push(alphabet[Math.floor(Math.random() * alphabet.length)])
    }
    hasilAlphabet.push(barisAlphabet);
  }
  return hasilAlphabet;
}

function checkAllConsonantInBox(area,array) {
  const vocal = 'AIUEO';
  const hasilAlphabets = array;

  for (let i=(Math.floor((area-1)/3))*3; i<=(Math.floor((area-1)/3))*3+2; i++) {
    for (let j=((area-1)%3)*3; j<=((area-1)%3)*3+2; j++) { 
      if (vocal.includes(hasilAlphabets[i][j])) {
        return false;
      }
    }
  } 

  return true;
}

function generateArrayOfObjectBox(array) {

const hasilAlphabets = array;
console.log(hasilAlphabets);
const hasilList = [];

for (let area=1; area<=9; area++ ) {
  let hasilDictionary = {};
  let value = [];
  for (let i=(Math.floor((area-1)/3))*3; i<=(Math.floor((area-1)/3))*3+2; i++) {
      for (let j=((area-1)%3)*3; j<=((area-1)%3)*3+2; j++) { 
        value.push(hasilAlphabets[i][j]);
      }
  }
  hasilDictionary['box_area'] = area;
  hasilDictionary['value'] = value;
  hasilDictionary['all_consonant_in_box'] = checkAllConsonantInBox(area,array);
  hasilList.push(hasilDictionary);
}
return hasilList; 
}

console.log(generateArrayOfObjectBox(generateAlphabetBoard()));