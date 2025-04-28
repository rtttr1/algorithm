const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/11441-합 구하기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input[1];
const [M] = input[2];
const section = input.slice(3);
arr.unshift(0);

for (let i = 2; i < arr.length; i++) {
  arr[i] = arr[i] + arr[i - 1];
}

section.forEach((coor) => {
  const [x, y] = coor;
  console.log(arr[y] - arr[x - 1]);
});
