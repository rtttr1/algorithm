const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : 'js/17609-회문/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((list) => list.split(' '));

const [T] = input[0];
const arr = input.slice(1).map(String);

arr.forEach((l) => {
  let left = 0,
    right = l.length - 1,
    flag = 0;

  for (let i = 0; i < l.length / 2; i++) {
    if (l[left] === l[right]) {
      left++;
      right--;
      continue;
    }

    if (flag === 0) {
      flag = 1;

      if (l[left + 1] === l[right] || l[left] === l[right - 1]) {
        let a = left + 2;
        let b = right - 1;

        while (a < b) {
          if (l[a] === l[b]) {
            a++;
            b--;
          } else {
            flag = 2;
            break;
          }
        }

        if (flag === 1) {
          break;
        } else if (flag === 2) {
          if (l[left] === l[right - 1]) {
            a = left + 1;
            b = right - 2;

            while (a < b) {
              if (l[a] === l[b]) {
                a++;
                b--;
              } else break;
            }
            if (a >= b) {
              flag = 1;
              break;
            }
          }
        }
      }
    } else {
      flag = 2;
      break;
    }
  }

  console.log(flag);
});
