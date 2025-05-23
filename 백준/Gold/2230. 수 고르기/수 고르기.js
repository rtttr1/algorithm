const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/2230-수 고르기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input
  .slice(1)
  .flatMap(Number)
  .sort((a, b) => a - b);

let [left, right, answer] = [0, 1, 2000000000];

while (left < N - 1) {
  // 두 수의 차가 M 미만일때
  if (arr[right] - arr[left] < M) {
    if (right === N - 1) {
      left++;
      continue;
    }
    right++;
    continue;
  }

  // 두 수의 차가 M 이상일떄
  if (arr[right] - arr[left] < answer) {
    answer = arr[right] - arr[left];
  }

  left++;
  continue;
}

console.log(answer);
