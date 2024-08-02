#write a program to print the unique of values of a dictionary,(you must use two dictionary do this)
dictionary={}
while True:
    key=input("enter key or 'stop' to finish  ")
    if key.lower()=='stop':
        break
    value=input('input value:')
    dictionary[key]=value
print(dictionary)    

b={}
count={}

for i in dictionary.values():
    count.setdefault(i,0)
    count[i]=count[i]+1
i=0
for k,v in count.items():
    if v==1:
        b.update({i:k})
        i=i+1
for i in b.values():
    print(i,end=" ")        
