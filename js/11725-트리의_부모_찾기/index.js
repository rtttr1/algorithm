const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : '11725-트리의_부모_찾기/input.txt',
  )
  .toString()
  .trim('')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));

const N = Number(input[0]);

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

  length() {
    return this.tailIndex - this.headIndex;
  }
}

const graph = Array.from({ length: N + 1 }, () => new Array().fill([]));

input.slice(1).forEach((list) => {
  graph[list[0]].push(list[1]);
  graph[list[1]].push(list[0]);
});

const answer = Array.from({ length: N + 1 }, () => 0);
const queue = new Queue();

queue.enqueue([1, graph[1]]);

while (queue.length()) {
  const [node, arr] = queue.dequeue();

  arr.forEach((elem) => {
    if (!answer[elem]) {
      answer[elem] = node;
      queue.enqueue([elem, graph[elem]]);
    }
  });
}

answer.forEach((elem, index) => {
  if (index > 1) {
    console.log(elem);
  }
});
