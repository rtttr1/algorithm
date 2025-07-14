const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/28118-안전한 건설 계획/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input.slice(1);

const parent = Array.from({ length: N }, () => -1);
let answer = 0;

const find = (x) => {
  if (parent[x] < 0) return x;
  return find(parent[x]);
};

const union = (x, y) => {
  const a = find(x);
  const b = find(y);

  if (a == b) return;

  if (parent[a] > parent[b]) {
    parent[b] += parent[a];
    parent[a] = b;
  } else {
    parent[a] += parent[b];
    parent[b] = a;
  }
};

arr.forEach((data) => union(data[0] - 1, data[1] - 1));

// 안이어진 집합의 개수 구하기
parent.forEach((num) => {
  if (num < 0) answer++;
});

// 두 집합 사이에 하나의 간선을 두면 다음 작업은 0의 비용
console.log(answer - 1);
