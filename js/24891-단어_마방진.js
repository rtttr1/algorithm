const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let count = 0;
  let L, N;
  const words = [];
  for await (const line of rl) {
    if (count === 0) {
      [L, N] = line.split(' ').map(Number);
    } else {
      words.push(line.split('').map(String));
    }
    count++;
    if (count >= N + 1) {
      rl.close();
    }
  }

  words.sort();

  // 백트래킹 최악 -> 20! * O(N^2)
  const Back = (s, visited) => {
    // 마방진 개수 다 차면 마방진인지 확인
    if (s.length === L) {
      if (isMabang(s)) {
        s.forEach((list) => console.log(list.join('')));
        process.exit();
      }
      return;
    }

    for (let i = 0; i < N; i++) {
      if (!visited[i]) {
        s.push(words[i]);
        visited[i] = true;
        Back(s, visited);
        s.pop();
        visited[i] = false;
      }
    }
  };

  // 마방진인지 확인 O(N^2)
  const isMabang = (graph) => {
    for (let i = 0; i < L; i++) {
      for (let j = i + 1; j < L; j++) {
        if (graph[i][j] !== graph[j][i]) {
          return false;
        }
      }
    }
    return true;
  };

  const s = [];
  const visited = Array.from({ length: L }, () => false);
  Back(s, visited);

  console.log('NONE');

  process.exit();
})();
