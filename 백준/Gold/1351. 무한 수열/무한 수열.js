const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1351-무한 수열/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, P, Q] = input[0];
if (N === 0) console.log(1);
else if (N === 1) console.log(2);
else {
  const map = new Map();
  map.set(0, 1);
  map.set(1, 2);

  const dfs = (i) => {
    if (map.has(i)) return map.get(i);

    map.set(i, dfs(Math.floor(i / P)) + dfs(Math.floor(i / Q)));
    return map.get(i);
  };

  dfs(N);
  console.log(map.get(N));
}
