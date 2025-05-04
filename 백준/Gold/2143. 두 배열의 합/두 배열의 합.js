const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/2143-두 배열의 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T] = input[0];
const [n] = input[1];
const A = input[2];
const [m] = input[3];
const B = input[4];

const AprefixSum = Array.from({ length: n + 1 }, () => 0);
const BprefixSum = Array.from({ length: m + 1 }, () => 0);

for (let i = 1; i < n + 1; i++) {
  AprefixSum[i] = AprefixSum[i - 1] + A[i - 1];
}

for (let i = 1; i < m + 1; i++) {
  BprefixSum[i] = BprefixSum[i - 1] + B[i - 1];
}

const AMap = new Map();
const BMap = new Map();

for (let i = 0; i < n + 1; i++) {
  for (let j = i + 1; j < n + 1; j++) {
    const num = AprefixSum[j] - AprefixSum[i];
    AMap.set(num, AMap.get(num) + 1 || 1);
  }
}

for (let i = 0; i < m + 1; i++) {
  for (let j = i + 1; j < m + 1; j++) {
    const num = BprefixSum[j] - BprefixSum[i];
    BMap.set(num, BMap.get(num) + 1 || 1);
  }
}

let answer = 0;

AMap.forEach((value, key) => {
  answer += BMap.get(T - key) * value || 0;
});

console.log(answer);
