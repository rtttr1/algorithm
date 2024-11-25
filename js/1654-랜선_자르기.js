const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N, K;
  const arr = [];

  for await (const line of rl) {
    if (count === 0) {
      [K, N] = line.split(' ').map(Number);
    } else {
      arr.push(+line);
    }

    count++;
    if (count >= K + 1) {
      rl.close();
    }
  }

  const decision = (meter) => {
    const amount = arr.reduce((acc, cur) => acc + Math.floor(cur / meter), 0);
    return N <= amount;
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
