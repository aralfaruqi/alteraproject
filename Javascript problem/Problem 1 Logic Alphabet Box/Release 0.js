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

console.log(generateAlphabetBoard());