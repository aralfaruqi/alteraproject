// callback
const beli = require('./beli');

let sandal = {
  item: 'sandal',
  harga: 2000,
  waktu: 2000,
};

let tas = {
  item: 'tas',
  harga: 2000,
  waktu: 2000,
};

let kaos = {
  item: 'kaos',
  harga: 2000,
  waktu: 2000,
};

let jaket = {
  item: 'jaket',
  harga: 2000,
  waktu: 2000,
};

let topi = {
  item: 'topi',
  harga: 2000,
  waktu: 2000,
};

beli(9000, sandal, function(kembalianSandal) {
  beli(kembalianSandal, tas, function(kembalianTas) {
    beli(kembalianTas, kaos, function(kembalianKaos) {
      beli(kembalianKaos, jaket, function(kembalianJaket) {
        beli(kembalianJaket, topi, function(kembalianTopi) {
          console.log(`Kembalian membeli sandal, tas, kaos, jaket dan topi adalah ${kembalianTopi}`)
        });
      });
    });    
  });
});
