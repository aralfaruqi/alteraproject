function beliPromise(uang, obj) {
    return new Promise((resolve, reject) => {
      console.log(`Saya pergi membeli ${obj.item}`)
      setTimeout(function() {
        // your code here
        uang -= obj.harga
        if (uang<0) {
          reject(`uang tidak cukup untuk membeli ${obj.item}, sisa kembalian ${uang+obj.harga}` )
        }
        else {
          resolve(uang)
        }
      }, obj.waktu);
    });
  }
  
  module.exports = beliPromise;