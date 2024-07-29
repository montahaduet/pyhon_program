f=open('numbers','w')
f.write('12321')
f.close()

f=open('numbers','r')
some_list=list(f.read())
f.close()

palindromic=True

for i in range(int(len(some_list)/2)):
    if some_list[i]!=some_list[len(some_list)-i-1]:
        palindromic=False
if palindromic:
    f=open('numbers','a')
    f.write('Yes')
    f.close()
else:
    f=open('numbers','w')
    for i in range(len(some_list)):
        f.write('0')
          

