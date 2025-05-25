const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/2531-회전 초밥/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, d, k, c] = input[0];
const arr = input.slice(1).flatMap(Number);

const map = new Map();
for (let i = 0; i < k; i++) {
  map.set(arr[i], map.get(arr[i]) + 1 || 1);
}

let [answer, index] = [map.size + (map.get(c) ? 0 : 1), 0];

while (index < N - 1) {
  if (map.get(arr[index]) == 1) map.delete(arr[index]);
  else map.set(arr[index], map.get(arr[index]) - 1);

  index++;

  map.set(arr[(index + k - 1) % N], map.get(arr[(index + k - 1) % N]) + 1 || 1);
  answer = Math.max(map.size + (map.get(c) ? 0 : 1), answer);
}

console.log(answer);
