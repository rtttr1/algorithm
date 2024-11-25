const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N, M, arr;

  for await (const line of rl) {
    if (count === 0) {
      N = +line;
    } else if (count === 1) {
      arr = line.split(' ').map(Number);
    } else {
      M = +line;
    }

    count++;
    if (count >= 3) {
      rl.close();
    }
  }

  const decision = (amount) => {
    const total = arr.reduce(
      (acc, cur) => (cur <= amount ? acc + cur : acc + amount),
      0,
    );
    return total <= M;
  };

  let start = 1;
  let end = Math.max(...arr);
  let result;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (decision(mid)) {
      result = mid;
      start = mid + 1;
    } else end = mid - 1;
  }

  console.log(result);
  process.exit();
})();
