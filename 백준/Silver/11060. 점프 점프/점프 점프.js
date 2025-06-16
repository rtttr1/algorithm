const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/11060-점프 점프/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));

const N = input[0];
const arr = input[1];

const dp = Array.from({ length: N }, () => 10e9);
dp[0] = 0;

if (N == 1) console.log(0);
else {
  for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < i + 1 + arr[i]; j++) {
      if (j >= N) break;

      dp[j] = Math.min(dp[i] + 1, dp[j]);
    }
  }

  if (dp[N - 1] == 10e9) console.log(-1);
  else console.log(dp[N - 1]);
}
