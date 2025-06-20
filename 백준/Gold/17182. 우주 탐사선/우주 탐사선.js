const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/17182-우주 탐사선/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, K] = input[0];
const arr = input.slice(1);

for (let k = 0; k < N; k++) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
    }
  }
}

// 백트래킹으로 모든 경우의 수 돌려보기?? N이 10개니까 시간복잡도 충분히 통과!
let answer = 10e9;
const visited = Array.from({ length: N }, () => false);
visited[K] = true;

const back = (node, count, time) => {
  if (count == N) {
    answer = Math.min(answer, time);
    return;
  }

  for (let i = 0; i < N; i++) {
    if (visited[i]) continue;

    visited[i] = true;
    back(i, count + 1, time + arr[node][i]);
    visited[i] = false;
  }
};

back(K, 1, 0);

console.log(answer);
