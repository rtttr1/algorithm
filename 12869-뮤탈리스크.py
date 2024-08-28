import sys 

N = int(sys.stdin.readline().strip())

HP = list(map(int, sys.stdin.readline().strip().split(' ')))
HP.extend([0,0])

dp = [[[0]*61 for _ in range(61)] for _ in range(61)]
dp[HP[0]][HP[1]][HP[2]] = 1
comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0 :
                for attack in comb :
                    ii = i - attack[0] if i - attack[0] >= 0 else 0 
                    jj = j - attack[1] if j - attack[1] >= 0 else 0 
                    kk = k - attack[2] if k - attack[2] >= 0 else 0 
                    if dp[ii][jj][kk] == 0 or dp[ii][jj][kk] > dp[i][j][k]+1 :
                        dp[ii][jj][kk] = dp[i][j][k] + 1
print(dp[0][0][0]-1)