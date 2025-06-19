const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/17136-색종이 붙이기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const graph = input;
const papers = [0, 0, 0, 0, 0];

const isRect = (x, y, l) => {
  let flag = true;
  for (let i = x; i <= x + l; i++) {
    for (let j = y; j <= y + l; j++) {
      if (graph[i][j] == 0) {
        flag = false;
        break;
      }
    }
    if (!flag) break;
  }

  return flag;
};

const fill = (x, y, l, value) => {
  for (let i = x; i <= x + l; i++) {
    for (let j = y; j <= y + l; j++) {
      graph[i][j] = value;
    }
  }
};

let answer = 100;
const back = (count, idx) => {
  if (count > answer) return;

  if (idx === coors.length) {
    if (answer > count) answer = count;
    return;
  }

  let index = idx;

  while (graph[coors[index][0]][coors[index][1]] == 0) {
    index++;
    if (index === coors.length) {
      if (answer > count) answer = count;
      return;
    }
  }

  const [x, y] = coors[index];

  for (let l = 4; l >= 0; l--) {
    if (papers[l] == 5 || x + l >= 10 || y + l >= 10) continue;

    if (isRect(x, y, l)) {
      papers[l]++;
      fill(x, y, l, 0);
      back(count + 1, index + 1);
      papers[l]--;
      fill(x, y, l, 1);
    }
  }
};

const coors = [];
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    if (graph[i][j] == 1) coors.push([i, j]);
  }
}

back(0, 0);
if (answer == 100) {
  console.log(-1);
} else {
  console.log(answer);
}
