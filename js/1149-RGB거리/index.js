const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

const N = input[0];
const RGBS = input.slice(1);

const dp = Array.from({ length: N }, () => new Array(3).fill(0));

dp[0] = RGBS[0];

for (let i = 1; i < N; i++) {
  for (let j = 0; j < 3; j++) {
    dp[i][j] =
      RGBS[i][j] + Math.min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]);
  }
}
console.log(Math.min(...dp[N - 1]));
