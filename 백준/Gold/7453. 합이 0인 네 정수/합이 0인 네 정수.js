const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/7453-합이 0인 네 정수/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input.slice(1);
const A = [],
  B = [],
  C = [],
  D = [];

let answer = 0;

arr.forEach((temp) => {
  A.push(temp[0]);
  B.push(temp[1]);
  C.push(temp[2]);
  D.push(temp[3]);
});

const ABMap = new Map();

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    ABMap.set(A[i] + B[j], ABMap.get(A[i] + B[j]) + 1 || 1);
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (ABMap.get((C[i] + D[j]) * -1)) answer += ABMap.get((C[i] + D[j]) * -1);
  }
}

console.log(answer);
