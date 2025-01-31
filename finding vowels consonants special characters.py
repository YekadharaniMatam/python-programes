s=input('enter your name')
p=c=sp=0
for i in s:
    if i in('aeiouAEIOU'):
        p=p+1
        print(i,'is vowel')
    elif i in('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
        c=c+1
        print(i,'is consonant')
    else:
        sp=sp+1
        print(i,'is special character')
print('the vowels are',p)
print('the consonants are',c)
print('the special characters are',sp)
    
