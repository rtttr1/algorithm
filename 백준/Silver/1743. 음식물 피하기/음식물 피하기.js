const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/1743-음식물 피하기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M, K] = input[0];
const coors = input.slice(1);

const graph = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => '.'),
);

coors.forEach((coor) => (graph[coor[0] - 1][coor[1] - 1] = '#'));

const visited = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => false),
);

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

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

let answer = 0;

const BFS = (sx, sy) => {
  const q = new Queue();
  let count = 1;

  q.enqueue([sx, sy, 1]);
  visited[sx][sy] = true;

  while (q.getLength()) {
    const [x, y] = q.dequeue();

    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];

      if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) continue;

      if (graph[nx][ny] == '#') {
        q.enqueue([nx, ny]);
        count++;
        visited[nx][ny] = true;
      }
    }
  }

  return count;
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (graph[i][j] == '#' && !visited[i][j]) {
      const temp = BFS(i, j);
      if (temp > answer) answer = temp;
    }
  }
}

console.log(answer);
