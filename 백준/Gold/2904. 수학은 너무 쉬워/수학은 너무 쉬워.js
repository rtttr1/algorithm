const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/2904-수학은 너무 쉬워/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input[1];

const MAX = 1000000;
const isPrime = Array.from({ length: MAX + 1 }, () => true);
const prime = [];

// 에네토스테스체
for (let i = 2; i <= MAX; i += 1) {
  if (isPrime[i]) {
    prime.push(i);
    for (let j = i * i; j <= MAX; j += i) {
      isPrime[j] = false;
    }
  }
}

const primeCount = Array.from({ length: N }, () => new Map());

// 각 숫자 소인수 분해
arr.forEach((num, index) => {
  for (let i = 0; i < prime.length; i++) {
    if (prime[i] >= num) {
      if (num !== 1) {
        primeCount[index].set(
          prime[i],
          (primeCount[index].get(prime[i]) || 0) + 1,
        );
      }
      break;
    }
    while (num % prime[i] == 0) {
      primeCount[index].set(
        prime[i],
        (primeCount[index].get(prime[i]) || 0) + 1,
      );
      num /= prime[i];
    }
  }
});

const gcd = new Map();

// gcd 구하기
prime.forEach((p) => {
  const count = primeCount.reduce(
    (acc, _, index, map) => acc + (map[index].get(p) || 0),
    0,
  );
  if (count !== 0 && Math.floor(count / N) > 0) {
    gcd.set(p, Math.floor(count / N));
  }
});

let sum = 0;
let gcdNum = 1;

gcd.forEach((count, prime) => {
  if (count > 0) {
    gcdNum *= Math.pow(prime, count);
    primeCount.forEach((primeMap) => {
      const diff = primeMap.get(prime) || 0;
      sum += Math.max(0, count - diff);
    });
  }
});
console.log(gcdNum, sum);
