a,amount=[int(x) for x in input().split()]
price=list(map(int,input().rstrip().split()))
volume=list(map(int,input().rstrip().split()))

dp={}

for i in range(len(price)):
    if price[i] in dp.keys():
        dp[price[i]]=max((dp.get(price[i],0)),volume[i])
    else:
        dp[price[i]]=volume[i]
#print(dp)
price=list(dp.keys())
#print(price)
volume=list(dp.values())
dp.clear()
#print(dp)
mp={}
for i in range(len(volume)):
    if volume[i] in mp.keys():
        mp[volume[i]]=min((mp.get(volume[i],0)),price[i])
    else:
        mp[volume[i]]=price[i]
#print(mp)

mp=sorted(mp.items(),key=lambda t:(t[0],t[1]))
#print(mp)
mp=dict(mp)
price=list(mp.values())
volume=list(mp.keys())
mp.clear()
#print(price)
#print(volume)
price.sort(reverse=True)
volume.sort(reverse=True)
#print(price)
#print(volume)

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
        print("Element not found")
print(s)
