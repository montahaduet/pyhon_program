def fib(num):
    if num==0:
        return 0
    else:
        x=0
        y=1
        print(x)
        print(y)
        for i in range(1,num):
            z=x+y
            x=y
            y=z
            print(z)
num=int(input("Enter the number: "))
print("Fibonacci number are: ")
fib(num)            

