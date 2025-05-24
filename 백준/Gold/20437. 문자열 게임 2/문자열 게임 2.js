const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/20437-문자열 게임 2/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' '));

const [T] = input[0];

const arr = input.slice(1).flat();

for (let t = 0; t < T; t++) {
  const [W, K] = [arr[t * 2], arr[t * 2 + 1]];
  let [long, short] = [-1, 100001];
  const wordMap = new Map();

  for (let i = 0; i < W.length; i++) {
    wordMap.set(W[i], wordMap.get(W[i]) + 1 || 1);
  }

  const words = [];
  wordMap.forEach((v, key) => {
    if (v >= K) words.push(key);
  });

  if (!words.length) console.log(-1);
  else {
    words.forEach((word) => {
      let [left, right, count] = [0, 0, 0];
      if (W[0] === word) count++;

      while (left < W.length && right < W.length) {
        if (count == K) {
          while (true) {
            if (W[left] == W[right]) break;
            left++;
          }
          if (W[left] === W[right] && W[left] === word && count == K) {
            long = Math.max(long, right - left + 1);
            short = Math.min(short, right - left + 1);
            left++;
            count--;
            continue;
          }
        }

        right++;
        if (W[right] === word) count++;
      }
    });

    console.log(short, long);
  }
}
