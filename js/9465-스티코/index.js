const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '11404-플로이드/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' ').map(Number));
  