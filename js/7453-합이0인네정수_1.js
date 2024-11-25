const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let n;
  const A = [],
    B = [],
    C = [],
    D = [];

  for await (const line of rl) {
    if (count === 0) {
      n = +line;
    } else {
      const temp = line.split(' ').map(Number);
      A.push(temp[0]);
      B.push(temp[1]);
      C.push(temp[2]);
      D.push(temp[3]);
    }

    count++;
    if (count >= n + 1) {
      rl.close();
    }
  }

  const arrayAB = [],
    arrayCD = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      arrayAB.push(A[i] + B[j]);
      arrayCD.push(C[i] + D[j]);
    }
  }
  arrayAB.sort((a, b) => a - b);
  arrayCD.sort((a, b) => a - b);
  const N = arrayAB.length;
  let answer = 0;
  let left = 0,
    right = arrayAB.length - 1;

  while (left < N && right >= 0) {
    if (arrayAB[left] + arrayCD[right] === 0) {
      answer++;
      left++;
      right--;
    } else if (arrayAB[left] + arrayCD[right] > 0) right--;
    else if (arrayAB[left] + arrayCD[right] < 0) left++;
  }
  console.log(answer);
  process.exit();
})();
