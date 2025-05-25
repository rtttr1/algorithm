const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/11728-배열 합치기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const A = input[1];
const B = input[2];

const arr = [];

let [a, b] = [0, 0];

while (a < N && b < M) {
  if (A[a] >= B[b]) {
    arr.push(B[b]);
    b++;
  } else {
    arr.push(A[a]);
    a++;
  }
}

if (a < N) {
  for (let i = a; i < N; i++) {
    arr.push(A[i]);
  }
} else if (b < M) {
  for (let i = b; i < M; i++) {
    arr.push(B[i]);
  }
}

console.log(arr.join(' '));
