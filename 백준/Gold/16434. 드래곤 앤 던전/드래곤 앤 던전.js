const fs = require('fs');
const input = fs
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/16434-드래곤 앤 던전/input.txt',
  )
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map((x) => BigInt(x)));

const [N, ATK] = input[0];
const arr = input.slice(1);

const MAX = BigInt('1000000000000000000'); // 1e18

function game(HP) {
  let hp = HP;
  let attack = ATK;
  for (let i = 0; i < Number(N); i++) {
    const [t, a, h] = arr[i];

    if (t === 2n) {
      attack += a;
      hp = hp + h > HP ? HP : hp + h;
      continue;
    }

    if (t === 1n) {
      // 몬스터 공격 횟수 계산
      let attackCount;
      if (h % attack === 0n) {
        attackCount = h / attack - 1n;
      } else {
        attackCount = h / attack;
      }
      hp -= attackCount * a;
      if (hp <= 0n) return false;
    }
  }
  return true;
}

let left = 1n;
let right = MAX;
let ans = MAX;

while (left <= right) {
  let mid = (left + right) / 2n;

  if (game(mid)) {
    ans = mid;
    right = mid - 1n;
  } else {
    left = mid + 1n;
  }
}

console.log(ans.toString());
