const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/1699-제곱수의 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];

const dp = Array.from({ length: N + 1 }, () => N);

for (let i = 1; i <= Math.sqrt(N); i++) {
  dp[i * i] = 1;
}

for (let i = 1; i <= N; i++) {
  for (let j = 1; j * j < i; j++) {
    if (dp[i] > dp[i - j * j] + 1) dp[i] = dp[i - j * j] + 1;
  }
}

console.log(dp[N]);
