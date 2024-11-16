const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '11403-경로찾기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));

const N = +input[0];
const graph = input.slice(1);

for (let k = 0; k < N; k++) {
  for (let a = 0; a < N; a++) {
    for (let b = 0; b < N; b++) {
      graph[a][b] = Math.max(graph[a][b], graph[a][k] && graph[k][b]);
    }
  }
}
graph.forEach(elem => console.log(elem.join(' ')));
