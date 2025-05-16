const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/3908-서로 다른 소수의 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T] = input[0];
const test = input.slice(1);
const answer = Array.from({ length: T }, () => 0);

const MAX = 1120;
isPrime = Array.from({ length: MAX + 1 }, () => true);
prime = [];

for (let i = 2; i <= MAX; i++) {
  if (isPrime[i]) {
    prime.push(i);
    for (let j = i * i; j <= MAX; j += i) {
      isPrime[j] = false;
    }
  }
}

const dp = Array.from({ length: 15 }, () =>
  Array.from({ length: MAX + 1 }, () => 0),
);

dp[0][0] = 1;

for (let i = 0; i < prime.length; i++) {
  for (let j = MAX; j >= prime[i]; j--) {
    for (let k = 1; k < 15; k++) {
      dp[k][j] += dp[k - 1][j - prime[i]];
    }
  }
}

test.forEach((arr) => {
  const [n, k] = arr;

  console.log(dp[k][n]);
});
