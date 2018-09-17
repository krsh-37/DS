#!/bin/python3

import os
import sys
def equalStacks(h1, h2, h3):
    c=0
    s1,s2,s3=[],[],[]
    s1.append(h1.pop()),s2.append(h2.pop()),s3.append(h3.pop())
    for i in range(1,len(h1)+1):
        x=h1.pop()
        s1.append(x+s1[-1])
    #print(s1)
    for i in range(1,len(h2)+1):
        x=h2.pop()
        s2.append(x+s2[-1])
    for i in range(1,len(h3)+1):
        x=h3.pop()
        s3.append(x+s3[-1])
    s1=set(s1)
    x=list(s1.intersection(set(s2).intersection(set(s3))))
    print(max(x))
    
if __name__ == '__main__':
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)