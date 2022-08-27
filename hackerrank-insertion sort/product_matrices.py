n=int(input())
for i in range(n):
    r1,c1=[int(x) for x in input().split()]
    arr1=[]
    for i in range(r1):
        row=list(map(int,input().rstrip().split()))
        arr1.append(row)
        
    r2,c2=[int(x) for x in input().split()]
    arr2=[]
    for i in range(r2):
        row=list(map(int,input().rstrip().split()))
        arr2.append(row)
    #multiplication
    arr3=[[0 for i in range(c2)]for j in range(r1)]
    #print(arr3)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                arr3[i][j]+=(arr1[i][k]*arr2[k][j])
    
    for i in range(r1):
        for j in range(c2):
            print(arr3[i][j],end=' ')
        print()
        
