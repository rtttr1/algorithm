const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/1484-다이어트/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' ').map(Number));

const [G] = input[0];
const answer = [];
for (let i = 1; i < Math.sqrt(G); i++) {
  if (G % i != 0) continue;

  const presentW = (i + G / i) / 2;
  if (Number.isInteger(presentW)) answer.push(presentW);
}

if (answer.length == 0) {
  console.log(-1);
} else {
  answer.reverse();
  answer.forEach((w) => console.log(w));
}
