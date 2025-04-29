const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/3020-개똥벌레/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [N, H] = input[0];
const arr = input.slice(1).map(Number);

const down = Array.from({ length: H }, () => 0);
const up = Array.from({ length: H }, () => 0);

arr.forEach((num, index) => {
  if (index % 2 === 0) {
    down[num - 1] += 1;
  } else {
    up[H - num] += 1;
  }
});

// 바닥 검사
for (let i = H - 2; i >= 0; i -= 1) {
  down[i] = down[i] + down[i + 1];
}
// 천장 검사
for (let i = 1; i < H; i++) {
  up[i] = up[i] + up[i - 1];
}

min = 10e9;
answer = 0;
for (let i = 0; i < H; i++) {
  if (up[i] + down[i] === min) {
    answer += 1;
    continue;
  }

  if (up[i] + down[i] < min) {
    min = up[i] + down[i];
    answer = 1;
  }
}
console.log(min, answer);
