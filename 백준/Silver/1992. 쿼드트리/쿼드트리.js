const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1992-쿼드트리/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' '));

const [N] = input[0];
const arr = input.slice(1).map((temp) => Array.from(temp[0]).map(Number));

const divide_conquer = (sx, sy, ex, ey) => {
  // base case
  if (ex - sx === 1) return arr[sx][sy];

  // 모두 같은 숫자인지 확인
  let flag = true;
  const num = arr[sx][sy];

  for (let i = sx; i < ex; i++) {
    for (let j = sy; j < ey; j++) {
      if (arr[i][j] !== num) {
        flag = false;
        break;
      }
    }
    if (!flag) break;
  }

  // 같은 숫자면 압축
  if (flag) {
    return num;
  }

  // 분할
  const interval = (ex - sx) / 2;
  const leftTop = divide_conquer(sx, sy, ex - interval, ey - interval);
  const rightTop = divide_conquer(sx, sy + interval, ex - interval, ey);
  const leftDown = divide_conquer(sx + interval, sy, ex, ey - interval);
  const rightDown = divide_conquer(sx + interval, sy + interval, ex, ey);

  // 정복
  return '(' + leftTop + rightTop + leftDown + rightDown + ')';
};

const answer = divide_conquer(0, 0, N, N);
console.log(answer);