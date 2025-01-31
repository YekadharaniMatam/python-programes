s1=int(input('enter 1st subject marks'))
s2=int(input('enter 2st subject marks'))
s3=int(input('enter 3st subject marks'))
s4=int(input('enter 4st subject marks'))
s5=int(input('enter 5st subject marks'))
sum=s1+s2+s3+s4+s5
avg=sum/5
if(avg>=90 and avg<=100):
    print("outstanding")
elif(avg>=80 and avg<=89):
    print("excellent")
elif(avg>=70 and avg<=79):
    print("very good")
elif(avg>=60 and avg<=69):
    print("good")
elif(avg>=50 and avg<=49):
    print('pass')
else:
    print('fail')
