d = int(input())
t = [0]*d
for i in range(d):
    t[i] = int(input())
d = min(t)
if d < -15:
    print("YES")
else:
    print("NO")