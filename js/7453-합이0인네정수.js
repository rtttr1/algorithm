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

  arrayCD.sort((a, b) => a - b);

  const upper = (target, arr) => {
    start = 0;
    end = arr.length;

    while (start < end) {
      let mid = Math.floor((start + end) / 2);

      if (arr[mid] <= target) start = mid + 1;
      else end = mid;
    }
    return start;
  };

  const lower = (target, arr) => {
    start = 0;
    end = arr.length;

    while (start < end) {
      let mid = Math.floor((start + end) / 2);

      if (arr[mid] < target) start = mid + 1;
      else end = mid;
    }
    return start;
  };

  let answer = 0;

  for (let i = 0; i < arrayCD.length; i++) {
    const low = lower(-arrayAB[i], arrayCD);
    const up = upper(-arrayAB[i], arrayCD);
    answer += up - low;
  }

  console.log(answer);
  process.exit();
})();
