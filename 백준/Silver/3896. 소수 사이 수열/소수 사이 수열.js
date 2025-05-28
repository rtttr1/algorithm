const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/3896-소수 사이 수열/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [T] = input[0];
const arr = input.slice(1).flat();

const MAX = 1299709;

const isPrime = Array.from({ length: MAX + 1 }, () => true);
const prime = [];

for (let i = 2; i < MAX + 1; i++) {
  if (isPrime[i]) prime.push(i);
  for (let j = i * i; j < MAX + 1; j += i) {
    isPrime[j] = false;
  }
}

for (let t = 0; t < T; t++) {
  let [left, right] = [0, prime.length - 1];
  const target = arr[t];

  if (prime.includes(target)) {
    console.log(0);
    continue;
  }

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (target <= prime[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  console.log(prime[right + 1] - prime[right]);
}
