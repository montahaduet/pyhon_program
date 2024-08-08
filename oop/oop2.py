class StoryBook:
#spicial method is used for setting the instance variables
    def __init__(self,name,price,author_name):
        #print('i am being called with instance/object creation')
        self.name=name
        self.price=price
        self.author_name=author_name
        self.publishing_year=2020

 
# creating an instance/object of the class
book_1=StoryBook('hamlet',350,'shakespeares')
book_2=StoryBook('kalid',200,'robin')

book_1.name='mun'

print(book_1.name)
print(book_2.name)
print(book_1.publishing_year)
