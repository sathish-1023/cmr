a,amount=[int(x) for x in input().split()]
#print(a,b)
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
#print(mp)
#print(price)
mini=min(tuple(price))
#print(mini)
#print(volume)
i=len(price)-1
s=0
while(amount>=mini or i>=0):
    for _ in range(amount//price[i]):
        s+=volume[i]
        amount-=price[i]
    i-=1
print(s)







        
        
    
