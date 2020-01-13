// ------library chalk----------
const chalk = require("chalk");

console.log(chalk.green('Apa Kabar'));
console.log(chalk.hex('#DEADED').bold('Jangan Lupa Senyum!'));
console.log(chalk.rgb(123, 45, 67).underline('Bawa Kabar Baik'));
console.log(chalk.keyword('orange')('Anak Senja'));
console.log(chalk.blue('Lautan Teduh'));

// -----library moment--------
const moment = require("moment");

console.log(moment().format('MMMM Do YYYY, h:mm:ss a'));
console.log(moment("20111031", "YYYYMMDD").fromNow());
console.log(moment().subtract(10, 'days').calendar()); 
console.log(moment().add(1, 'days').calendar()); 

// -----library node-emoji----
const emoji = require("node-emoji");

console.log(emoji.which(emoji.get('coffee')));
console.log(emoji.get(':fast_forward:')); 
console.log(emoji.emojify('I :heart: :coffee:!'));
console.log(emoji.random());

// ------library hasha--------
const hasha = require("hasha");

console.log(process.stdin.pipe(hasha.stream()).pipe(process.stdout));
console.log(hasha('unicorn'));

(async () => {
    const hash = await hasha.fromFile('album-lelaku.jpg', {algorithm: 'md5'});
    console.log(hash);
})();

// ------library request------
const request = require('request');

request('http://www.espn.com', function (error, response, body) {
  console.log('error:', error); 
  console.log('statusCode:', response && response.statusCode); 
  console.log('body:', body); 
});






