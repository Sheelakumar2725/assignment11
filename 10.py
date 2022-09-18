#loops
#octal equivalent of a given decimal number.

print("Enter the Decimal Number: ")
n = int(input())
i = 0
octnum = []
while n>0:
    rem = n%8
    octnum.insert(i, rem)
    i = i+1
    n = int(n/8)

print("\nEquivalent Octal Value is: ")
i = i-1
while i>=0:
    print(octnum[i], end="")
    i = i-1
print()
