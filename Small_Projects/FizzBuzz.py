def Modulos (num):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif (num % 5 == 0):
        print("Buzz")
    elif (num % 3 == 0):
        print("Fizz")
    else:
        print(i)


num=int(input("Enter desired loops (min. 16): "))
for i in range(1,num):
    Modulos(i)