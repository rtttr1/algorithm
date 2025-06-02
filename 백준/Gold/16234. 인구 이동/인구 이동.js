const readline = require('readline');

class Queue {
  constructor() {
    this.items = {};
    this.tail = 0;
    this.head = 0;
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

  peek() {
    return this.items[this.head];
  }

  getLength() {
    return this.tail - this.head;
  }
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let N, L, R;
  const arr = [];

  for await (const line of rl) {
    if (count === 0) {
      [N, L, R] = line.split(' ').map(Number);
    } else {
      arr.push(line.split(' ').map(Number));
    }

    count++;
    if (count >= N + 1) {
      rl.close();
    }
  }

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  let answer = 0;

  while (true) {
    let flag = false;

    const visited = Array.from({ length: N }, () => Array(N).fill(false));

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (!visited[i][j]) {
          const queue = new Queue();
          queue.enqueue([i, j]);

          const temp = [];
          temp.push([i, j]);

          let cnt = 1;
          let sum = arr[i][j];
          visited[i][j] = true;

          while (queue.getLength()) {
            const [x, y] = queue.dequeue();

            for (let i = 0; i < 4; i++) {
              let nx = x + dx[i];
              let ny = y + dy[i];

              if (nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny])
                continue;

              const minus = Math.abs(arr[nx][ny] - arr[x][y]);

              if (minus >= L && minus <= R) {
                visited[nx][ny] = true;
                queue.enqueue([nx, ny]);
                temp.push([nx, ny]);
                cnt++;
                sum += arr[nx][ny];
                flag = true;
              }
            }
          }

          const num = Math.floor(sum / cnt);

          temp.forEach(([x, y]) => {
            arr[x][y] = num;
          });
        }
      }
    }

    if (!flag) break;
    answer++;
  }

  console.log(answer);
  process.exit();
})();
