const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/12852-1로 만들기 2/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];

const dp = Array.from({ length: N + 1 }, () => N);
dp[0] = 0;
dp[1] = 0;

for (let i = 1; i < N; i++) {
  if (i + 1 <= N && dp[i + 1] > dp[i] + 1) dp[i + 1] = dp[i] + 1;
  if (i * 2 <= N && dp[i * 2] > dp[i] + 1) dp[i * 2] = dp[i] + 1;
  if (i * 3 <= N && dp[i * 3] > dp[i] + 1) dp[i * 3] = dp[i] + 1;
}

let path = '' + N;
let num = N;

while (true) {
  if (num === 1) break;

  if (dp[num - 1] === dp[num] - 1) num--;
  else if (dp[num / 2] === dp[num] - 1) num /= 2;
  else if (dp[num / 3] === dp[num] - 1) num /= 3;

  path += ' ' + num;
}

console.log(dp.at(-1));
console.log(path);
