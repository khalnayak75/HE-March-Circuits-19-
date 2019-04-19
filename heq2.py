line1= input()
line2= input()
line3= input()
lt1= line1.split(' ')
lt1= [int(i) for i in lt1]
lt2= line2.split(' ')
lt2= [int(i) for i in lt2]
lt3= line3.split(' ')
lt3= [int(i) for i in lt3]
c= len(lt2)
nc=0
g=0
f=0
for i in range(1,c):
    for td in lt3:
        if td<=(lt2[i]-lt2[i-1]):
            nc+=1
            lt3.remove(td)
            f+=1
        if f!=0:
            g+=1
        f=0
    if g>lt1[2]:
        break
print (nc)
        
    
