#!/bin/python3
#Here, we compare top of the two stacks and popping the min. val of two. But this sucks.
#two stacks s1 = [16,1,1,1,8] and s2 = [8,8,3,5,9] and max sum = 20.
# you will select from s2 because 8 < 16.
#You will end up removing 3 ints from s2.
#Contrary to that if you pick from s1, you end up picking 4 ints.
#thanks to the people of disscussion section.
#credits to kewltek

import os
import sys

def twoStacks(x, a, b, m):
    a=a[::-1]
    b=b[::-1]
    c,s=0,0
    total = 0
    atmp = []
    for i in range(n):
        val = a.pop()
        if total + val > x:
            break
        total += val 
        atmp.append(val)

    max_count = len(atmp)
    cur_count = max_count
    while m:
        if total + b[-1] <= x:
            total += b.pop() 
            m -= 1
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        total -= aval
        cur_count -= 1
    return (max_count)
    '''
    while(1): 
        if((a[-1]<=b[-1] and s+a[-1]<x)):
            t=a.pop()
            c+=1
            s+=t
            print(c,t,a)
        elif((a[-1]>b[-1] and s+b[-1]<x)):
            t=b.pop()
            c+=1
            s+=t
            print(c,t,b)
        else:
            #print(s,a[-1],b[-1])
            #print(i+3)
            break
            
    return c
    '''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b, m)
        fptr.write(str(result) + '\n')
#fptr.write(str(result) + '\n
        #print(result+1)

    fptr.close()
