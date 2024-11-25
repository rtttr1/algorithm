const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '15681-트리와_쿼리/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, R, Q] = input[0];
const graph = Array.from({ length: N + 1 }, () => []);

for (let i = 0; i < N - 1; i++) {
  graph[input[i + 1][0]].push(input[i + 1][1]);
  graph[input[i + 1][1]].push(input[i + 1][0]);
}

const counts = Array.from({ length: N + 1 }, () => 0);

const DFS = (node) => {
  visited[node] = true;
  counts[node] = 1;

  for (i of graph[node]) {
    if (!visited[i]) {
      counts[node] += DFS(i);
    }
  }

  return counts[node];
};

const visited = Array.from({ length: N + 1 }, () => false);
DFS(R);

for (let i = 0; i < Q; i++) {
  console.log(counts[input[N + i]]);
}
