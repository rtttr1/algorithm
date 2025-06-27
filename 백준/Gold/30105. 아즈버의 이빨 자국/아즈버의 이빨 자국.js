const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/30105-아즈버의 이빨 자국/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input[1];
const answer = [];
const map = new Map();
const visited = new Map();

arr.forEach((num) => map.set(num, true));

const isValid = (diff) => {
  for (const [key, _] of map) {
    if (!map.has(key - diff) && !map.has(key + diff)) {
      return false;
    }
  }

  return true;
};

for (let i = 1; i < N; i++) {
  const diff = arr[i] - arr[0];

  if (visited.has(diff)) continue;

  if (isValid(diff)) {
    answer.push(diff);
  }

  visited.set(diff, true);
}

map.forEach((v, k) => {
  if (v.size == N) answer.push(k);
});

console.log(answer.length);
console.log(answer.join(' '));
