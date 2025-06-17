const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1987-알파벳/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' '));

const [R, C] = input[0];
const arr = input.slice(1).map((temp) => temp[0].split(''));
let answer = 0;
const visited = Array.from({ length: 26 }, () => false);

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

const Back = (x, y, count) => {
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];

    if (
      nx < 0 ||
      nx >= R ||
      ny < 0 ||
      ny >= C ||
      visited[arr[nx][ny].charCodeAt() - 65]
    ) {
      if (count > answer) answer = count;
      continue;
    }

    visited[arr[nx][ny].charCodeAt() - 65] = true;
    Back(x + dx[i], y + dy[i], count + 1);
    visited[arr[nx][ny].charCodeAt() - 65] = false;
  }
};

visited[arr[0][0].charCodeAt() - 65] = true;
Back(0, 0, 1);
console.log(answer);
