const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/7795-먹먹/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T] = input[0];

for (let t = 0; t < T; t++) {
  const [N, M] = input[t * 3 + 1];
  const A = input[t * 3 + 2];
  const B = input[t * 3 + 3];

  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);

  let [a, b, answer] = [0, 0, 0];

  while (a < N && b < M) {
    if (A[a] > B[b]) {
      while (A[a] > B[b + 1]) b++;
      answer += b + 1;
      a++;
      continue;
    } else {
      a++;
    }
  }

  console.log(answer);
}
