def prime(num):
    for i in range(2,num):
        flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print("number is not prime")
    else:
        print("number is  prime")

num=int(input())
prime(num)

        
