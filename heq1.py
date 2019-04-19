def sm(n):
    s=0
    for i in range (1,n+1):
        s= s+i
    return s
def pr(n):
    p=1
    for i in range (1,n+1):
        p=p*i
    return p
num= int(input('Enter a Number: '))
f1= sm(num)
f2= pr(num)
if f2%f1==0:
    print ('YES')
else:
    print ('NO')
