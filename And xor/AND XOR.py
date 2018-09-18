n = int(input())
l1=list(map(int, input().rstrip().split()))
l2= []
#print(l1)
m=-1
for i in l1:
    while len(l2)!= 0:
        top = l2[-1]
        mi = top ^ i
       # print(top,i,"=",mi)
        if mi > m:
            m=mi
        if top > i:
            l2.pop()
        else:
            break
    l2.append(i)
    
print(m)