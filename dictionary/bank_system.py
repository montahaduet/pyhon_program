bank_user={'sam':4325,'mun':3409,'rohit':20198}
print('wellcome to the bank.')
while True:
    print('What do you like to do?')
    print(' '+'1.VIEW THE BALANCE')
    print(' '+'2.VIEW ALL BANK INFO')
    print(' '+'3.update balance')
    print(' '+'4.EXIT')

    decision=input()
    if decision=='1':
        print("enter your name: ")
        k=input()
        if k in bank_user.keys():
            print(k+' your account balance is '+str(bank_user[k]))
        else:
            print('The user can not be found.would you like to add new user at this account?')
            decision=input()
            if decision=='yes':
                k=input('enter your name ')  
                v=input('enter your balance')
                bank_user.update({k:v})
            else:
                print('Would like to exit?')
                decision =input()
                if decision=='yes':
                    break
    elif decision=='2':
        for k, v in bank_user.items():
            print('username: '+str(k)+'bank_balance:'+str(v))
    elif decision=='3':
        print('Enter your name: ')
        k=input()  
        if k in bank_user.keys():
            print('Do you want to add or3 subtract from your saving ')
            decision=input()
            if decision=='add':
                temp_balance=bank_user[k]
                extra=input('enter the amount you want to add: ')
                (bank_user[k])=temp_balance+int(extra)
                print('blance updated. it is: ')
                print (bank_user[k])
            elif decision=='sub':
                temp_balance=bank_user[k]
                extra=input('enter the amount you want to subtract: ')
                bank_user[k]=temp_balance+int(extra)
                print('blance updated. it is: ')
                print(bank_user[k])
        else:
            print('there is no such account in the database')
    elif decision=='4':
        break



                 

    
   
