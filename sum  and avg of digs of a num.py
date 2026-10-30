c=246
sum,count=0,0
while c>0:
    d=c%10
    sum+=d
    count+=1
    c//=10

print(sum)
avg=sum/count
print(avg)

#output:
12
4.0

    
