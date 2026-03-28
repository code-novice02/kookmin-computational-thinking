orig=int(input())
count=0
result=100
while(1):
    if(count==0): temp=orig
    else: temp=result
    if(temp<10):
        result=temp*11
    else:
        result=(temp%10*10)+(temp%10+temp//10)%10
    count+=1
    if(orig==result): break
print(count)
