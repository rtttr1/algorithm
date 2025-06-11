const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/16397-탈출/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, T, G] = input[0];
const visited = Array.from({ length: 100000 }, () => 99999);

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

const q = new Queue();
let answer = -1;

q.enqueue([N, 0]);
visited[N] = 0;

while (q.getLength()) {
  let [num, count] = q.dequeue();

  if (num > 99999 || count > T) {
    continue;
  }

  // 성공
  if (num == G) {
    answer = count;
    break;
  }

  for (let i = 0; i < 2; i++) {
    if (i == 0) {
      let temp = num;
      temp++;
      if (visited[temp] <= count + 1) continue;

      q.enqueue([temp, count + 1]);
      visited[temp] = count + 1;
    } else if (i == 1 && num != 0) {
      num = num * 2;

      if (num > 99999) {
        break;
      }

      num = num - Math.pow(10, num.toString().length - 1);

      if (visited[num] <= count + 1) break;
      q.enqueue([num, count + 1]);
      visited[num] = count + 1;
    }
  }
}

if (answer != -1) {
  console.log(answer);
} else {
  console.log('ANG');
}
