#if-else statement
"""
if 2<1:
    print("2 is large")
elif 1<0:
    print("2 is smalar")
else:
    print("another number")

"""
# if else----------------------------------- 
"""
print("enter command")
robot_move=input()
if robot_move=='front':
    print('moving front')
elif robot_move=='back':
    print('moving back')  
else:
    print("still now")  
"""
#while loop-------------------------------------

# x=0
# while(x<10):
#     print(x)
#     x=x+1

#------


########for loo-----------------------------
# for i in range(1,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)

while True:
    print("who are you?")
    name=input()
    if name!='batman':
        continue
    print('there name is '+name+ 'what is your passcode')
    pasecode=input()
    if pasecode=='nullvalue':
        break
print('hello')





    



