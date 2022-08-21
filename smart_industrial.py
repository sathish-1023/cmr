a,amount=[int(x) for x in input().split()]
price=list(map(int,input().rstrip().split()))
volume=list(map(int,input().rstrip().split()))
diff=[]
for i in range(len(price)):
    diff.append(volume[i]-price[i])
#print(diff)
mini=min(tuple(price))

s=0
while(amount>=mini):
    try:
       
        ind=diff.index(max(tuple(diff)))
        s+=volume[ind]
        amount-=price[ind]
        price.remove(price[ind])
        volume.remove(volume[ind])
        diff.remove(diff[ind])
    except ValueError as e:
        print("elemnt not found")
print(s)
