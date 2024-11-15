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

console.log(graph)