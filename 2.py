#loops
#to calculate the sum of squares of first N natural numbers

n=int(input("enter a number:"))
sum=0
for e in range(0,n+1,1):
    k=e*e
    sum=sum+k
print('the sum of squares of first n natural numbers is:',sum)
