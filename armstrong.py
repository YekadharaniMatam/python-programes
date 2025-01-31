n=int(input('enter a value'))
sum=0
n1=n
while(n>0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if(sum==n1):
    print(n1,'is armstrong')
else:
    print('not armstrong')
