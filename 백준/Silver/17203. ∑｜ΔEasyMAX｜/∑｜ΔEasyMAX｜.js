const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/17203-easy/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, Q] = input[0];
const arr = input[1];
const intervals = input.slice(2);

const temp = Array.from({ length: N - 1 }, () => 0);
const prefixSum = Array.from({ length: N }, () => 0);

for (let i = 0; i < N - 1; i++) {
  temp[i] = Math.abs(arr[i + 1] - arr[i]);
}
for (let i = 1; i < N; i++) {
  prefixSum[i] = temp[i - 1] + prefixSum[i - 1];
}

intervals.forEach((coor) => {
  const [i, j] = coor;
  if (j - 1 < i) {
    console.log(0);
  } else {
    console.log(prefixSum[j - 1] - prefixSum[i - 1]);
  }
});
