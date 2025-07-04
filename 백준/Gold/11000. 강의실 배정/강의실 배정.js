const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/11000-강의실 배정/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N] = input[0];
const arr = input.slice(1);

class minHeap {
  constructor() {
    this.heap = [];
  }

  getSize() {
    return this.heap.length;
  }

  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  pop() {
    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  getMin() {
    return this.heap[0];
  }

  bubbleUp() {
    let idx = this.getSize() - 1;

    while (idx > 0) {
      let pIndex = Math.floor((idx - 1) / 2);
      if (this.heap[pIndex] <= this.heap[idx]) break;
      [this.heap[idx], this.heap[pIndex]] = [this.heap[pIndex], this.heap[idx]];
      idx = pIndex;
    }
  }

  bubbleDown() {
    let idx = 0;

    while (true) {
      let leftIdx = idx * 2 + 1;
      let rightIdx = idx * 2 + 2;
      let smallest = idx;

      if (
        leftIdx < this.heap.length &&
        this.heap[smallest] > this.heap[leftIdx]
      ) {
        smallest = leftIdx;
      }
      if (
        rightIdx < this.heap.length &&
        this.heap[smallest] > this.heap[rightIdx]
      ) {
        smallest = rightIdx;
      }
      if (smallest === idx) break;

      [this.heap[smallest], this.heap[idx]] = [
        this.heap[idx],
        this.heap[smallest],
      ];
      idx = smallest;
    }
  }
}

arr.sort((a, b) => {
  if (a == b) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
});

const minQ = new minHeap();
minQ.add(arr[0][1]);

for (let i = 1; i < N; i++) {
  if (minQ.getMin() <= arr[i][0]) {
    minQ.pop();
  }
  minQ.add(arr[i][1]);
}

console.log(minQ.getSize());
