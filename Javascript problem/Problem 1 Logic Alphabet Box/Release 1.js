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
  
function checkAllConsonantInBox(area) {
const vocal = 'AIUEO';
const hasilAlphabets = generateAlphabetBoard();
console.log(hasilAlphabets);

for (let i=(Math.floor((area-1)/3))*3; i<=(Math.floor((area-1)/3))*3+2; i++) {
    for (let j=((area-1)%3)*3; j<=((area-1)%3)*3+2; j++) { 
    if (vocal.includes(hasilAlphabets[i][j])) {
        return false;
    }
    }
} 
return true;
}

console.log(checkAllConsonantInBox(7));


