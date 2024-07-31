# import pprint as pp
# text='this is a simple text to TEST the code.'
# letters={}
# for i in text:
#     letters.setdefault(i,0)
#     letters[i]=letters[i]+1
# pp.pprint(letters)

#this program simulated a password protected app access

password_bank={'sam':1234, 'mun':456,'shain':987}
matched=False
x=0
print('enter your name:')
while x<5:
    name=input()
    if name in password_bank:
        for i in range(0,3):
            print('enter your password:')
            password=input()
            if int(password) in password_bank.values():
                matched=True
                print('Access Granted.')
                break
            else:
                print('Wrong password.Enter Again:'+'You have '+str(2-i)+' tries left')
    else:
        print('There is no such name in the password_bank.Try again...')
    x=x+1

    if matched:
        break

            


