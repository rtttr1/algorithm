const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/13975-파일 합치기3/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

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
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

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

const [T] = input[0];

for (let t = 0; t < T; t++) {
  const [K] = input[t * 2 + 1];
  const arr = input[t * 2 + 2];

  const q = new minHeap();
  let answer = 0;
  arr.forEach((num) => q.add(num));

  for (let i = 0; i < K - 1; i++) {
    let cost1 = q.pop();
    let cost2 = q.pop();
    answer += cost1 + cost2;

    q.add(cost1 + cost2);
  }
  console.log(answer);
}
