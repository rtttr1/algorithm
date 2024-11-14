const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '14502-연구소/input.txt',
  )
  .toString()
  .trim()
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));

const [N, M] = [...input[0]];
const graph = input.slice(1);

class Queue {
  constructor(item) {
    this.items = { item };
    this.headIndex = 0;
    this.tailIndex = 0;
  }
  enqueue(item) {
    this.items[this.tailIndex] = item;
    this.tailIndex++;
  }
  dequeue() {
    const item = this.items[this.headIndex];
    delete this.items[this.headIndex];
    this.headIndex++;
    return item;
  }
  getLength() {
    return this.headIndex - this.tailIndex;
  }
}

// 0인 안전지대 찾는 함수
const findSafe = (graph) => {
  return graph.reduce(
    (acc, cur) =>
      cur.reduce((acc2, cur2) => (cur2 === 0 ? acc2 + 1 : acc2 + 0), 0) + acc,
    0,
  );
};

const BFS = (graph) => {
  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  const queue = new Queue();

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] === 2) {
        queue.enqueue([i, j]);
      }
    }
  }

  while (queue.getLength()) {
    const [x, y] = queue.dequeue();
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];

      if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }

      if (!graph[nx][ny]) {
        queue.enqueue([nx, ny]);
        graph[nx][ny] = 2;
      }
    }
  }
  return graph;
};

let answer = 0;

const Back = (count, graph) => {
  if (count === 3) {
    answer = Math.max(answer, findSafe(BFS(graph.map((v) => [...v]))));
    return;
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] === 0) {
        graph[i][j] = 1;
        count += 1;
        Back(count, graph);
        graph[i][j] = 0;
        count -= 1;
      }
    }
  }
};

Back(0, graph);

console.log(answer);
