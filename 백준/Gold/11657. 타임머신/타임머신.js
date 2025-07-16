const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/11657-타임머신/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input.slice(1);
const INF = 10e9;

const dist = Array.from({ length: N + 1 }, () => INF);

const bellmanFord = (start) => {
  dist[start] = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      const [node, nextNode, cost] = arr[j];

      if (dist[node] !== INF && dist[node] + cost < dist[nextNode]) {
        dist[nextNode] = dist[node] + cost;

        if (i == N - 1) return false;
      }
    }
  }
  return true;
};

if (bellmanFord(1)) {
  for (let i = 2; i < N + 1; i++) {
    if (dist[i] == INF) {
      console.log(-1);
    } else {
      console.log(dist[i]);
    }
  }
} else {
  console.log(-1);
}
