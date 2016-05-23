import random
def countEvens(n):
    A=randomList(n)
    count=0
    for i in A:
        if i%2==0:
            count+=1
    return count

def myMin(n):
    A=randomList(n)
    mymin=A[0]
    for i in range(1,len(A)):
        if A[i]<A[i-1]:
            mymin=A[i]
    return mymin

def myMax(n):
    A=randomList(n)
    mymax=A[0]
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            mymax=A[i]
    return mymax

def median(n):
    A=randomList(n)
    med=0
    for j in range(len(A)-1):
        for i in range(len(A)-j-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
    if len(A)%2!=0:
        med=A[len(A)//2]
    else:
        med=(A[len(A)//2]+A[len(A)//2-1])/2
    return med

def secondBiggest(n):
    A=randomList(n)
    A.remove(max(A))
    secondbiggest=max(A)
    return secondbiggest

def LIS(n):
    A = randomList(n)
    length = len(A)
    countList = [1 for i in range(length)]
    for i in range(1,length):
        if A[i] > A[i-1]:
            countList[i] = countList[i-1] + 1
    count= max(countList)
    return count

def dot(n):
    A=randomList(n)
    B=randomList(n)
    dp=0
    for i in range (len(A)):
        dp+=A[i]*B[i]
    return dp

def instersect1(n):
    A=randomList(n)
    B=randomList(n)
    C=[]
    for i in A:
        for j in B:
            if i==j:
                C.append(i)
    return C

def instersect2(n):
    A=randomList(n)
    B=randomList(n)
    C=[]
    A.sort()
    B.sort()
    a_index=0
    b_index=0
    while a_index<len(A) and b_index<len(B):
        a=A[a_index]
        b=B[b_index]
        if a==b:
            C.append(a)
            a_index+=1
            b_index+=1
        elif a<b:
            a_index+=1
        else:
            b_index+=1
    return C

def fib1(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib1(n-1)+fib1(n-2)

def fib2(n):
    A=[0,1,1]
    for i in range (n-2):
        A.append(A[-1]+A[-2])
    return A

def randomList(n):
    A = [i for i in range(n)]
    random.shuffle(A)
    return A
