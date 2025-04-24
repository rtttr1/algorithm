const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/1747-소수&팰린드롬/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const MAX = 1003002;
isPrime = Array.from({ length: MAX }, () => true);
prime = [];

for (let i = 2; i <= MAX; i += 1) {
  if (isPrime[i]) {
    prime.push(i);
    for (let j = i * i; j <= MAX; j += i) {
      isPrime[j] = false;
    }
  }
}

for (let i = 0; i <= prime.length; i += 1) {
  if (prime[i] < N) continue;

  let temp = Number(String(prime[i]).split('').reverse().join(''))

  if(temp === prime[i]) {
    console.log(prime[i])
    break
  }
}
