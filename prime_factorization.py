n=int(input())
ans=[]
f=[]
while n>1:
    for i in range(2, n+1):
        while n%i==0:
            n=int(n/i)
            ans.append(i)
new=set(ans)
new=list(new)
new.sort()
for i in new:
    a=ans.count(i)
    if a==0:
        f=f
    elif a==1:
        f.append(f"{i}")
    else:
        f.append(f"{i}^{a}")
print("*".join(f))
    