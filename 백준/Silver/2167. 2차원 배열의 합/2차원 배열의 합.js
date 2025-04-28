const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/2167-2차원 배열의 합/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, M] = input[0];
const arr = input.slice(1, 1 + N);
const [K] = input[N + 1];
const section = input.slice(N + 2);

const prefixSum = Array.from({ length: N + 1 }, () =>
  Array.from({ length: M + 1 }, () => 0),
);

for (let i = 1; i < N + 1; i++) {
  for (let j = 1; j < M + 1; j++) {
    prefixSum[i][j] =
      prefixSum[i][j - 1] +
      prefixSum[i - 1][j] -
      prefixSum[i - 1][j - 1] +
      arr[i - 1][j - 1];
  }
}

section.forEach((coor) => {
  const [i, j, x, y] = coor;

  console.log(
    prefixSum[x][y] -
      prefixSum[i - 1][y] -
      prefixSum[x][j - 1] +
      prefixSum[i - 1][j - 1],
  );
});
