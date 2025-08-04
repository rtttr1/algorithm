const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/2240-자두나무/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T, W] = input[0];
const arr = input.slice(1).flat();

const tree = Array.from({ length: 2 }, () =>
  Array.from({ length: T }, () => 0),
);
arr.forEach((num, index) => (tree[num - 1][index] = 1));

const dp = Array.from({ length: W + 1 }, () =>
  Array.from({ length: T }, () => 0),
);

dp[0][0] = tree[0][0];
dp[1][0] = tree[1][0];

for (let i = 2; i < W + 1; i++) {
  dp[i][i - 1] = dp[i - 1][i - 2] + tree[i % 2][i - 1];
}

for (let i = 1; i < T; i++) {
  dp[0][i] = tree[0][i] + dp[0][i - 1];
}

for (let i = 1; i < W + 1; i++) {
  for (let j = i; j < T; j++) {
    dp[i][j] = tree[i % 2][j] + Math.max(dp[i][j - 1], dp[i - 1][j - 1]);
  }
}

answer = 0;
for (let i = 0; i < W + 1; i++) {
  answer = Math.max(answer, dp[i][T - 1]);
}

console.log(answer);
