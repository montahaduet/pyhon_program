def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
result=fact(4)
print(result)   
