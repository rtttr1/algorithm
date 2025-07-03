const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1374-강의실/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

class MinHeap {
  constructor() {
    this.heap = [];
  }

  add(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  pop() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return min;
  }

  getMin() {
    return this.heap[0];
  }

  getSize() {
    return this.heap.length;
  }

  bubbleUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[parentIdx] <= this.heap[idx]) break;
      [this.heap[parentIdx], this.heap[idx]] = [
        this.heap[idx],
        this.heap[parentIdx],
      ];
      idx = parentIdx;
    }
  }

  bubbleDown() {
    let idx = 0;
    while (true) {
      let leftChild = 2 * idx + 1;
      let rightChild = 2 * idx + 2;
      let smallest = idx;

      if (
        leftChild < this.heap.length &&
        this.heap[leftChild] < this.heap[smallest]
      ) {
        smallest = leftChild;
      }
      if (
        rightChild < this.heap.length &&
        this.heap[rightChild] < this.heap[smallest]
      ) {
        smallest = rightChild;
      }
      if (smallest === idx) break;

      [this.heap[idx], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[idx],
      ];
      idx = smallest;
    }
  }
}

const [N] = input[0];
const arr = input.slice(1);

if (N == 1) console.log(1);
else {
  arr.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[2] - b[2];
    }
    return a[1] - b[1];
  });

  const minQueue = new MinHeap();
  minQueue.add(arr[0][2]);

  for (let i = 1; i < N; i++) {
    if (arr[i][1] >= minQueue.getMin()) {
      minQueue.pop();
      minQueue.add(arr[i][2]);
    } else {
      minQueue.add(arr[i][2]);
    }
  }

  console.log(minQueue.getSize());
}
