const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N;
  const foods = [];
  for await (const line of rl) {
    if (count === 0) {
      N = +line;
    } else {
      foods.push(line.split(' ').map(Number));
    }
    count++;
    if (count >= N + 1) {
      rl.close();
    }
  }
  
  const answer = [];

  const Back = (start, end, s) => {
    if (s.length === end) {
      const temp = s.reduce((acc, cur) => {
        return [acc[0] * cur[0], acc[1] + cur[1]];
      });
      answer.push(Math.abs(temp[1] - temp[0]));

      return;
    }

    for (let i = start; i < N; i++) {
      s.push(foods[i]);
      Back(i + 1, end, s);
      s.pop();
    }
  };

  for (let i = 1; i < N + 1; i++) {
    const s = [];
    Back(0, i, s);
  }

  console.log(Math.min(...answer));
  process.exit();
})();
