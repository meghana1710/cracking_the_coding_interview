l = [0]*10
n = "3211000"
flag = 0
for i in range(len(n)):
    l[i] = n.count(str(i))
for i in range(len(n)):
    if(int(n[i]) == l[i]):
        continue
    else:
        flag = 1
        break
if(flag):
    print("not")
else:
    print("yes")
