n = int(input())
x = n
count = 0
while n!=0:
    count +=1
    n = n//10
print(count)

while count>0:
    temp = x//(10**(count-1))
    if count ==1:
        print(temp)
    else:
        print(temp,end=",")
    
    x = x%(10**(count-1))
    #print("x",x)
    count-=1
    #print("count",count)
    
