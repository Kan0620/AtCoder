import math
P = [0.1, 0.3, 0.2, 0.4]
ans1 = 0
for p in P:
    ans1 += p*math.log(1/p)
print(1-ans1/4)
print(1-1.28/2)