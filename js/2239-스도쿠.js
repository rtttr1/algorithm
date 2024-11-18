const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;

  const sdocu = [];
  for await (const line of rl) {
    sdocu.push(line.split('').map(Number));
    count++;

    if (count === 9) {
      rl.close();
    }
  }

  console.log(sdocu);
  process.exit();
})();
