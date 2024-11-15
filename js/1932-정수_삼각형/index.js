const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '1932-정수_삼각형/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));

const N = +input[0];

const dp = Array.from({ length: N }, () => new Array(N).fill(0));

const tree = input.slice(1);

dp[0][0] = tree[0][0]

for (let i = 1; i < N; i++) {
  for (let j = 0; j <= i; j++) {
    if (j === 0) {
      dp[i][j] = dp[i - 1][j] + tree[i][j];
      continue;
    }
    dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + tree[i][j];
  }
}

console.log(Math.max(...dp[N - 1]));
