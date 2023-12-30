# The Kaprekar constant is a math problem, it says: every number with diferent digits (7834) after being
# sorted upwards (3478) and substracted from the downwards sorted list (8743) {8743-3478=5265} and repeating
# this operation with the new number will always leads us to the number 6174, this algorythm will tell us
# how many iterations will take to to get to the number.

# We define the function that uses the entry number
def kaprekar(n):
    # Iteration counter and the Kaprekar const
    count = 0
    while n != 6174:
        # Turn the number to a character list
        n = list(str(n).zfill(4))
        # Sort the lists and turn them into integer numbers.
        upward = int(''.join(sorted(n)))
        downward = int(''.join(sorted(n, reverse=True)))
        # subtraction and return the itineration count
        n = downward - upward
        print(downward," - ",upward," = ", n ,"\n")
        count += 1
    return count


def main():
    while True:
        n = input("four-digit number without repeating:\n")
        # we validate the number
        if len(set(n)) == 4 and len(n) == 4:
            # print the counter and break cicle
            print(f"It takes {kaprekar(int(n))} iterations to get to the Kaprekar number.")
            break
        else:
            # ask for a diferent and valid number
            print("Make sure it is a four-digit number without repeating.")

# in case this algorythm runs as a script we call the main function.
if __name__ == "__main__":
    main()


