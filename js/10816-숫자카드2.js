const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N, M;
  let cards, mCards;

  for await (const line of rl) {
    if (count === 0) {
      N = +line;
    } else if (count === 1) {
      cards = line.split(' ').map(Number);
    } else if (count === 2) {
      M = +line;
    } else {
      mCards = line.split(' ').map(Number);
    }

    count++;
    if (count >= 4) {
      rl.close();
    }
  }

  cards.sort();

  process.exit();
})();
