const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;

  const sdocu = [];
  for await (const line of rl) {
    sdocu.push(line.split('').map(Number));
    count++;

    if (count === 9) {
      rl.close();
    }
  }

  const check = (x, y, num) => {
    if (sdocu[x].includes(num)) {
      return false;
    }
    for (let i = 0; i < 9; i++) {
      if (sdocu[i][y] === num) {
        return false;
      }
    }
    for (let i = x * 3; i < (x + 1) * 3 - 1; i++) {
      for (let j = y * 3; j < (y + 1) * 3 - 1; j++) {
        if (sdocu[i][j] === num) {
          return false;
        }
      }
    }
    return true;
  };

  const Back = (index) => {
    // 탈출 조건
    if (index === arr.length - 1) {
      sdocu.forEach((list) => console.log(list.join('')));
      return;
    }

    for (let i = 1; i < 3; i++) {
      const [x, y] = arr[index];
      console.log(x, y, i);
      console.log(Math.floor(x / 3), Math.floor(y / 3), i);
      if (check(Math.floor(x / 3), Math.floor(y / 3), i)) {
        // console.log(x, y, i);
        sdocu[x][y] = i;
        Back(index + 1);
        sdocu[x][y] = 0;
      }
    }
  };

  // 스도쿠 숫자 넣어야하는 좌표 다 찾기
  const arr = [];
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (sdocu[i][j] === 0) {
        arr.push([i, j]);
      }
    }
  }

  console.log(arr);
  Back(0);
  process.exit();
})();
