const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1327-소트 게임/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

class Queue {
  constructor() {
    this.head = 0;
    this.tail = 0;
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

const [N, K] = input[0];
const arr = input[1];

const map = new Map();

const reverse = (arr, start) => {
  for (let i = 0; i < K / 2; i++) {
    const temp = arr[start + i];
    arr[start + i] = arr[start + K - i - 1];
    arr[start + K - i - 1] = temp;
  }
  return arr;
};

const correct = Array.from({ length: N }, (_, i) => i + 1).join('');
let answer = 10e9;

const BFS = () => {
  const q = new Queue();
  q.enqueue([arr, 0]);
  map.set(arr.join(''), true);

  while (q.getLength()) {
    const [nodes, count] = q.dequeue();

    if (correct === nodes.join('')) {
      answer = count;
      break;
    }

    for (let i = 0; i < N - K + 1; i++) {
      const temp = reverse(nodes.slice(), i);

      if (map.has(temp.join(''))) continue;

      map.set(temp.join(''), true);
      q.enqueue([temp, count + 1]);
    }
  }
};

BFS();

if (answer == 10e9) {
  console.log(-1);
} else {
  console.log(answer);
}
