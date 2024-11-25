const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : '1240-노드사이의_거리/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const graph = Array.from({ length: N + 1 }, () => new Array());

for (let i = 1; i < N; i++) {
  graph[input[i][0]].push([input[i][1], input[i][2]]);
  graph[input[i][1]].push([input[i][0], input[i][2]]);
}

const nodes = [];
for (let i = N; i < N + M; i++) {
  nodes.push(input[i]);
}

const dfs = (x, dist) => {
  if (visited[x]) return;
  visited[x] = true;
  distance[x] = dist;
  for (let [y, cost] of graph[x]) dfs(x, dist + cost);
};

nodes.forEach((elem) => {
  dfs(elem[0], 0);
});
// const BFS = (node, end) => {
//   const visited = Array.from({ length: N + 1 }, () => false);

//   const queue = [];
//   queue.push([node, 0]);
//   visited[node] = true;

//   while (queue.length) {
//     const [n, distance] = queue[0];
//     queue.shift();

//     if (n === end) return console.log(distance);

//     for (i of graph[n]) {
//       if (!visited[i[0]]) {
//         queue.push([i[0], distance + i[1]]);
//         visited[i[0]] = true;
//       }
//     }
//   }
// };

// nodes.forEach((elem) => BFS(elem[0], elem[1]));
