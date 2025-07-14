const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/24542-튜터 튜티 관곗의 수/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input.slice(1);

arr.sort((a, b) => {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
});

const parent = Array.from({ length: N }, () => -1);
let answer = 1;

const find = (x) => {
  if (parent[x] < 0) return x;
  return find(parent[x]);
};

const union = (x, y) => {
  const a = find(x);
  const b = find(y);

  if (a == b) {
    return;
  }

  if (parent[a] < parent[b]) {
    parent[a] += parent[b];
    parent[b] = a;
  } else {
    parent[b] += parent[a];
    parent[a] = b;
  }
};

arr.forEach((data) => union(data[0] - 1, data[1] - 1));

parent.forEach((num) => {
  if (num < 0) {
    answer = (Math.abs(num) * answer) % 1000000007;
  }
});

console.log(answer);
