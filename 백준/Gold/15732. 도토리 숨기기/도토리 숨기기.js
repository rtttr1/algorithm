const fs = require('fs');
const input = fs
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

const [N, K, D] = input[0];
const arr = input.slice(1);

const isPromising = (index) => {
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    const [start, end, step] = arr[i];

    if (index < start) continue;

    count += Math.floor((Math.min(end, index) - start) / step) + 1;
  }

  return count >= D;
};

let [left, right] = [0, N];

while (left + 1 < right) {
  const mid = Math.floor((left + right) / 2);
  if (isPromising(mid)) {
    right = mid;
  } else {
    left = mid;
  }
}

console.log(right);
