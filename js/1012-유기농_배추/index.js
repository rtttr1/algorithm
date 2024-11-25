const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '1012-유기농_배추/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const DFS = (x, y, visited, M, N, graph) => {
  // 반환
  if (x < 0 || x >= M || y < 0 || y >= N || visited[x][y]) return;

  // 방문체크
  visited[x][y] = true;

  // 자식 노드들을 DFS 돌리기
  if (graph[x][y]) {
    visited[x][y] = true;

    DFS(x + 1, y, visited, M, N, graph);
    DFS(x, y + 1, visited, M, N, graph);
    DFS(x - 1, y, visited, M, N, graph);
    DFS(x, y - 1, visited, M, N, graph);
  }
};

const T = +input[0];
let line = 1;

for (let k = 0; k < T; k++) {
  const [M, N, K] = input[line];
  const graph = Array.from({ length: M }, () => new Array(N).fill(0));

  for (let i = line + 1; i < K + line + 1; i++) {
    graph[input[i][0]][input[i][1]] = 1;
  }

  let answer = 0;
  const visited = Array.from({ length: M }, () => new Array(N).fill(false));

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (graph[i][j] === 1 && !visited[i][j]) {
        DFS(i, j, visited, M, N, graph);
        answer++;
      }
    }
  }
  console.log(answer);
  line += K + 1;
}
