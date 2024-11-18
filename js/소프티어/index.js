// Run by Node.js
const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let N;
  let graph = [];
  let count = 0;
  for await (const line of rl) {
    if (count === 0) {
      N = +line;
    } else {
      graph.push(line.split(' ').map(Number));
    }
    count++;
    if (count > N) {
      rl.close();
    }
  }

  class Queue {
    constructor() {
      this.items = {};
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
      return this.tailIndex - this.headIndex;
    }
  }

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];
  const BFS = (x, y) => {
    const queue = new Queue();
    queue.enqueue([x, y, 1]);
    visited[x][y] = true;
    let size = 0;
    while (queue.getLength()) {
      const [a, b] = [...queue.dequeue()];
      size++;
      for (let i = 0; i < 4; i++) {
        const [nx, ny] = [a + dx[i], b + dy[i]];

        if (
          nx < 0 ||
          nx >= N ||
          ny < 0 ||
          ny >= N ||
          visited[nx][ny] ||
          !graph[nx][ny]
        ) {
          continue;
        }
        if (graph[nx][ny]) {
          queue.enqueue([nx, ny]);
          visited[nx][ny] = true;
        }
      }
    }
    return size;
  };

  const answer = [];
  const visited = Array.from({ length: N }, () => new Array(N).fill(false));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j] && graph[i][j]) {
        answer.push(BFS(i, j));
        console.log(visited);
      }
    }
  }
  console.log(answer.length);
  console.log(answer.sort().join(' '));
  process.exit();
})();
