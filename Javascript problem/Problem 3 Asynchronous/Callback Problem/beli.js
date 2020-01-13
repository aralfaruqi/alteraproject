function beli(uang, obj, cb){
    console.log(`Saya pergi membeli ${obj.item}`)
  
    setTimeout(function(){
      // your code here
      uang -= obj.harga
      if (uang < 0) {
        console.log(`Uang tidak cukup untuk membeli ${obj.item}, sisa kembalian ${uang+obj.harga}`)
      }
      else {
        cb(uang)
      }
    }, obj.waktu);
  }
  
  module.exports = beli;
  