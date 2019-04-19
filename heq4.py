n= int(input())
ip= []
temp= []
for i in range(n):
    t= input()
    temp= t.split(' ')
    temp= [int(r) for r in temp]
    ip.append(temp)
c=1
for i in range(n):
    l1= ip[i]
    m1= (l1[3]-l1[1])/(l1[2]-l1[0])
    for j in range(i+1,n):
        l2= ip[j]
        m2= (l2[3]-l2[1])/(l2[2]-l2[0])
        if (m1/m2)==1:
            c+=1
print ('Max number of lines: ',c)
