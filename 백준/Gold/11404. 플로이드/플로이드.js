const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '11404-플로이드/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));
const INF = 1e9;
const N = +input[0];
const M = +input[1];

const graph = Array.from({ length: N + 1 }, () => new Array(N + 1).fill(INF));
for (let i = 1; i < N + 1; i++) {
  graph[i][i] = 0;
}

input
  .slice(2)
  .forEach(
    (elem) =>
      (graph[elem[0]][elem[1]] = Math.min(graph[elem[0]][elem[1]], elem[2])),
  );

// k는 이번단계에서 지나가는 노드의 번호
for (let k = 1; k < N + 1; k++) {
  // a에서 b를 1을 거쳐서 가는 것
  for (let a = 1; a < N + 1; a++) {
    for (let b = 1; b < N + 1; b++) {
      graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
    }
  }
}

for (let i = 0; i < N + 1; i++) {
  for (let j = 0; j < N + 1; j++) {
    if (graph[i][j] === INF) {
      graph[i][j] = 0;
    }
  }
}
graph.slice(1).forEach((list) => {
  console.log(list.slice(1).join(' '));
});
