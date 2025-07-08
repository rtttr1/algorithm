const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/16562-친구비/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M, K] = input[0];
const price = input[1];
const arr = input.slice(2);

const parent = Array.from({ length: N }, () => -1);

const find = (x) => {
  if (parent[x] < 0) return x;
  return find(parent[x]);
};

const union = (x, y) => {
  const a = find(x);
  const b = find(y);

  if (a == b) return;

  if (price[a] < price[b]) {
    parent[b] = a;
  } else {
    parent[a] = b;
  }
};

arr.forEach((data) => union(data[0] - 1, data[1] - 1));

let answer = 0;
for (let i = 0; i < N; i++) {
  if (parent[i] == -1) {
    answer += price[i];
  }
}

if (answer <= K) console.log(answer);
else console.log('Oh no');
