const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : '1991-트리순회/input.txt',
  )
  .toString()
  .trim(' ')
  .split('\n')
  .map((elem) => elem.split(' '));

const N = +input[0][0];
let result = ''
const tree = {};
for (let i = 1; i < N+1; i++) {
  const [node, left, right] = input[i];
  tree[node] = [left, right];
}

const preorder = (node) => {
  if (node === '.') {
    return;
  }
  result += node;
  preorder(tree[node][0]);
  preorder(tree[node][1]);
};
function inorder(node) {
  if (node === '.') return;
  const [left, right] = tree[node];
  inorder(left);
  result += node;
  inorder(right);
}

function postorder(node) {
  if (node === '.') return;
  const [left, right] = tree[node];
  postorder(left);
  postorder(right);
  result += node;
}
preorder('A');
result += '\n';
inorder('A');
result += '\n';
postorder('A')

console.log(result)
