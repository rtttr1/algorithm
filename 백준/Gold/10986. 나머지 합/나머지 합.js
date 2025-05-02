const { count } = require('console');

const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/10986-나머지 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input[1];
const countArr = Array.from({ length: M }, () => 0);
const remainArr = Array.from({ length: N }, () => 0);
const prefixSum = Array.from({ length: N }, () => 0);

arr.forEach((num, index) => (remainArr[index] = num % M));

countArr[remainArr[0]] += 1;
prefixSum[0] = remainArr[0];
for (let i = 1; i < N; i++) {
  prefixSum[i] = (remainArr[i] + prefixSum[i - 1]) % M;
  countArr[prefixSum[i]] += 1;
}

let answer = countArr[0];
let sum = 0;
for (let i = 0; i < N; i++) {
  const num = remainArr[i];
  sum = (sum + num) % M;
  countArr[sum]--;

  answer += countArr[sum];
}
console.log(answer);
