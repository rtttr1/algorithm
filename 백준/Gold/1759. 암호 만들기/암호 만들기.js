const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'js/1759-암호 만들기/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' '));

const [L, C] = input[0].map(Number);
const arr = input[1].sort();
const moum = ['a', 'e', 'i', 'o', 'u'];

const mo = arr.filter((t) => moum.includes(t));
const ja = arr.filter((t) => !moum.includes(t));

const temp = [];
const count = [0, 0];

const back = (temp, index) => {
  if (temp.length == L) {
    if (count[0] >= 1 && count[1] >= 2) {
      console.log(temp.join(''));
    }
    return;
  }

  for (let i = index; i < C; i++) {
    if (moum.includes(arr[i])) {
      count[0]++;
    } else {
      count[1]++;
    }
    temp.push(arr[i]);
    back(temp, i + 1);
    temp.pop();
    if (moum.includes(arr[i])) {
      count[0]--;
    } else {
      count[1]--;
    }
  }
};

back(temp, 0);
