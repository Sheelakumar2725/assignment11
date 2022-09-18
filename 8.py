#loops
#to sum of the digits in given number

n=int(input("enter a digit:"))
sum=0
while n>0:
    x=int(n%10)
    sum=sum+x
    n=n/10
    
print('the sum of given number is:',sum)
