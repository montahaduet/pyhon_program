class StoryBook:
#spicial method is used for setting the instance variables
    def __init__(self,name,price,author_name,author_born,publishing_year,no_of_pages):
        #print('i am being called with instance/object creation')
        self.name=name
        self.price=price
        self.author_name=author_name
        self.author_born=author_born
        self.publishing_year=2020
        self.no_of_pages=400
#regular method 1      
    def get_book_info(self):
        print(f'The book name:{self.name},price:{self.price}')
#regular method 2
    def get_author_info(self):
        print(f'The author name:{self.author_name},born:{self.author_born}')
# creating an instance/object of the class
book_1=StoryBook('hamlet',350,'shakespeares',1990,2020,400)
book_2=StoryBook('kalid',200,'robin',2010,2020,456)

#book_1.get_book_info()
StoryBook.get_book_info(book_1)
book_2.get_author_info()

