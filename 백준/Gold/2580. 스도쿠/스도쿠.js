const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/2580-스도쿠/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const sdocu = input;

const coors = [];

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (sdocu[i][j] == 0) {
      coors.push([i, j]);
    }
  }
}

const isBox = (x, y, num) => {
  const [col, row] = [Math.floor(x / 3), Math.floor(y / 3)];
  let flag = true;
  for (let i = 3 * col; i < 3 * (col + 1); i++) {
    for (let j = 3 * row; j < 3 * (row + 1); j++) {
      if (sdocu[i][j] == num) {
        flag = false;
        break;
      }
    }
    if (!flag) break;
  }

  return flag;
};

const isDir = (x, y, num) => {
  let flag = true;
  for (let i = 0; i < 9; i++) {
    if (sdocu[x][i] == num || sdocu[i][y] == num) {
      flag = false;
      break;
    }
  }

  return flag;
};

let flag = false;

const back = (idx) => {
  if (flag) return;

  if (idx === coors.length) {
    flag = true;
    return;
  }

  const [x, y] = [coors[idx][0], coors[idx][1]];

  for (let i = 1; i < 10; i++) {
    if (isBox(x, y, i) && isDir(x, y, i)) {
      sdocu[x][y] = i;
      back(idx + 1);

      if (flag) return;
      sdocu[x][y] = 0;
    }
  }
};

back(0);

sdocu.forEach((row) => console.log(row.join(' ')));
