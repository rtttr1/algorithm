const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/1780-종이의 개수/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input.slice(1);
const answer = [0, 0, 0];

const divide_conquer = (sx, sy, n) => {
  // base case 1개면 카운트
  if (n === 1) {
    answer[arr[sx][sy] + 1]++;
    return;
  }

  // 다 같은 종이인지 확인
  let count = 0;
  const flag = arr[sx][sy];
  for (let i = sx; i < sx + n; i++) {
    for (let j = sy; j < sy + n; j++) {
      if (arr[i][j] === flag) count++;
    }
  }

  // 다 같은 종이이면 카운트
  if (count === n * n) {
    answer[flag + 1]++;
    return;
  }

  // 분할 -> 종이를 9등분
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      divide_conquer(sx + i * (n / 3), sy + j * (n / 3), n / 3);
    }
  }
};

divide_conquer(0, 0, N);

answer.forEach((num) => console.log(num));
