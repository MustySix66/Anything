# If a number is pair it's going to be divided in 2, if it's an odd number, it's going to be multiplied x3 then added 1
# This exercise says that every number in this teorema will eventually came to an 4-2-1 cicle, this 
# Script will show every step taken until we get to the 4-2-1 cycle.

def collatz(n):
    i=1
    while n != 1:
        print(n)
        i+=1
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = 3*n + 1
    print(n)
    print("It took ",i, " steps to get into the bucle.")

# Test the function
var=int(input("Put any integer number: "))
collatz(var)

