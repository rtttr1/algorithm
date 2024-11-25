const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N, M, A;
  const B = [];

  for await (const line of rl) {
    if (count === 0) {
      [N, M] = line.split(' ').map(Number);
    } else if (count === 1) {
      A = line.split(' ').map(Number);
    } else {
      B.push(line.split(' ').map(Number));
    }

    count++;
    if (count >= M + 2) {
      rl.close();
    }
  }

  A.sort((a, b) => a - b);

  const upper = (target) => {
    start = 0;
    end = N - 1;

    while (start <= end) {
      let mid = Math.floor((start + end) / 2);

      if (A[mid] > target) end = mid - 1;
      else start = mid + 1;
    }
    return end;
  };

  const lower = (target) => {
    start = 0;
    end = N - 1;

    while (start <= end) {
      let mid = Math.floor((start + end) / 2);

      if (A[mid] >= target) end = mid - 1;
      else start = mid + 1;
    }
    return end;
  };

  for (let i = 0; i < M; i++) {
    if (B[i][0] === 1) console.log(N - lower(B[i][1]) - 1);
    else if (B[i][0] === 2) console.log(N - upper(B[i][1]) - 1);
    else console.log(upper(B[i][2]) - lower(B[i][1]));
  }

  process.exit();
})();
