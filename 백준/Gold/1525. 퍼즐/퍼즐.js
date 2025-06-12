const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1525-퍼즐/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const arr = input;

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const map = new Map();

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

const swap = (graph, a, b) => {
  const newGraph = graph.split('');
  newGraph[a] = newGraph[b];
  newGraph[b] = '0';

  return newGraph.join('');
};

const sortedList = '123456780';

const q = new Queue();

q.enqueue(arr.flat().join(''));
let answer = -1;
map.set(arr.flat().join(''), 0);

while (q.getLength()) {
  const graph = q.dequeue();

  if (graph === sortedList) {
    answer = map.get(graph);
    break;
  }

  const zero = graph.indexOf('0');
  const [x, y] = [Math.floor(zero / 3), zero % 3];

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3) continue;

    const swapGraph = swap(graph, x * 3 + y, nx * 3 + ny);

    if (map.has(swapGraph)) continue;

    q.enqueue(swapGraph);
    map.set(swapGraph, map.get(graph) + 1);
  }
}

console.log(answer);
