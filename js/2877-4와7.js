const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let K;
  for await (const line of rl) {
    K = +line;
    rl.close();
  }

  let n = 1;
  answer = '';
  while (K > 0) {
    const num = K % Math.pow(2, n);
    if (num > Math.pow(2, n - 1) || num === 0) {
      answer = '7' + answer;
    } else {
      answer = '4' + answer;
    }
    K -= Math.pow(2, n);
    n++;
  }
  console.log(answer);
  process.exit();
})();
