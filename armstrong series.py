for n in range(0,999+1):
    sum=0
    n1=n
    
    while(n>0):
        r=n%10
        sum=sum+r*r*r
        n=n//10
    if(sum==n1):
        print(n1)
        
