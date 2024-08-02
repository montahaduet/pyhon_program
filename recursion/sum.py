def sum(num):
    if num==0:
        return 0
    
    return num+sum(num-1)
num=int(input())  
print('sum= '+str(sum(num)))
    