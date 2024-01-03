# Question: BJ 1495 (https://www.acmicpc.net/problem/1495)
# Rank : Silver 3
# Algorithm : Math, Many conditions

import sys
input_val = sys.stdin.readline().split()

X, Y, W, S = map(int, input_val)
result=0

if Y>X:
    if 2*W>S:
        if S>W:
            result+=(X*S+(Y-X)*W)
        else:
            if (X+Y)%2==1 and X!=Y:
                result+=((Y-1)*S+W)
            else:
                result+=Y*S
    else:
        result+=((X+Y)*W)
else:
    if 2*W>S:
        if S>W:
            result+=(Y*S+(X-Y)*W)
        else:
            if (X+Y)%2==1 and X!=Y:
                result+=((X-1)*S+W)
            else:
                result+=X*S
    else:
        result+=((X+Y)*W)

print(result)    
