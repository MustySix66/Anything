number=int(input("How many numbers u wanna see? "))
manual=0
fibo=0
fiboNew=1
i=2
print(fibo)
while(i<=number):
    print(fiboNew)
    manual=fibo
    fibo=fiboNew
    fiboNew=manual+fibo
    i=i+1