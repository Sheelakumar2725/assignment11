#loops
#to calculate the sum of first N odd natural numbers

n=int(input("enter a number:"))
sum=0
for e in range(0,n+1,1):
    if e%2!=0:
        sum=sum+e
    
print('the sum of first n odd natural numbers is:',sum)
