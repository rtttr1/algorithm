const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/17425-약수의 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T] = input[0];
const arr = input.slice(1).map(Number);

const MAX = 1000000;
const divSum = Array.from({ length: MAX + 1 }, () => 1);
const prefixSum = Array.from({ length: MAX + 1 }, () => 0);

for (let i = 2; i <= MAX; i++) {
  for (let j = 1; j * i <= MAX; j++) {
    divSum[j * i] += i;
  }
}

for (let i = 1; i <= MAX; i++) {
  prefixSum[i] = divSum[i] + prefixSum[i - 1];
}

const answer = [];
arr.forEach((num) => {
  answer.push(prefixSum[num]);
});

console.log(answer.join('\n'));
