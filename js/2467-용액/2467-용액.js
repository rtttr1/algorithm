const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '2467-용액/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const N = +input[0];
const arr = input[1];

let [left, right, temp] = [0, N - 1, 10e9];
let answer;

while (left < right) {
  let sum = arr[left] + arr[right];

  if (Math.abs(sum) < Math.abs(temp)) {
    temp = sum;
    answer = [arr[left], arr[right]];
  }

  if (sum < 0) left++;
  else if (sum > 0) right--;
  else break;
}

console.log(answer.join(' '));
