const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/6593-상범 빌딩/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' '));

class Queue {
  constructor() {
    this.tail = 0;
    this.head = 0;
    this.items = {};
  }

  enqueue(item) {
    this.items[this.tail] = item;
    this.tail++;
  }

  dequeue() {
    const temp = this.items[this.head];
    delete this.items[this.head];
    this.head++;
    return temp;
  }

  getLength() {
    return this.tail - this.head;
  }
}

const findStart = (arr, L, R, C) => {
  for (let i = 0; i < L; i++) {
    for (let j = 0; j < R; j++) {
      for (let k = 0; k < C; k++) {
        if (arr[i][j][k] == 'S') {
          return [i, j, k];
        }
      }
    }
  }
};

const dx = [0, 0, 1, 0, -1, 0];
const dy = [0, 0, 0, 1, 0, -1];
const dz = [1, -1, 0, 0, 0, 0];
let s = 0;

while (true) {
  const [L, R, C] = input[s].map(Number);

  if (L == 0 && R == 0 && C == 0) break;

  const visited = Array.from({ length: L }, () =>
    Array.from({ length: R }, () => Array.from({ length: C }, () => false)),
  );

  const inputArr = input.slice(s + 1, s + (R + 1) * L);

  const arr = [];
  let layer = [];

  for (const row of inputArr) {
    const line = row[0];
    if (line === '') {
      if (layer.length > 0) arr.push(layer);
      layer = [];
    } else {
      layer.push([...line]);
    }
  }

  if (layer.length > 0) {
    arr.push(layer);
  }

  const [sz, sx, sy] = findStart(arr, L, R, C);

  const q = new Queue();
  q.enqueue([sz, sx, sy, 0]);
  visited[sz][sx][sy] = true;

  let answer = -1;

  while (q.getLength()) {
    const [z, x, y, count] = q.dequeue();

    if (arr[z][x][y] == 'E') {
      answer = count;
      break;
    }

    for (let i = 0; i < 6; i++) {
      const [nx, ny, nz] = [x + dx[i], y + dy[i], z + dz[i]];

      if (
        nx < 0 ||
        nx >= R ||
        ny < 0 ||
        ny >= C ||
        nz < 0 ||
        nz >= L ||
        visited[nz][nx][ny]
      )
        continue;

      if (arr[nz][nx][ny] !== '#') {
        q.enqueue([nz, nx, ny, count + 1]);
        visited[nz][nx][ny] = true;
      }
    }
  }

  if (answer == -1) {
    console.log('Trapped!');
  } else {
    console.log(`Escaped in ${answer} minute(s).`);
  }
  s += (R + 1) * L + 1;
}
