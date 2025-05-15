const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1351-무한 수열/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];

const dp = Array.from({ length: N + 1 }, () => BigInt(0));
dp[1] = BigInt(1);

if (N === 1) console.log(1);
else {
  for (let i = 2; i <= N; i++) {
    dp[i] = BigInt(dp[i - 1] + dp[i - 2]);
  }

  console.log(dp[N].toString());
}
