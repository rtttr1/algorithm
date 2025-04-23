const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/2960-에라토스테네스의 체/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, K] = input[0];

const MAX = N;
const isPrime = Array.from({ length: MAX + 1 }, () => true);
let count = 0;

for (let i = 2; i <= MAX; i += 1) {
  if (isPrime[i]) {
    for (let j = i; j <= MAX; j += i) {
      if (isPrime[j]) {
        count += 1;
        isPrime[j] = false;
        if (count === K) {
          console.log(j);
          process.exit(0);
        }
      }
    }
  }
}
