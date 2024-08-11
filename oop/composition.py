class StoryBook:
    no_of_books=0
    discount=0.5



    def __init__(self,name,price,author_name,author_born,publishing_year,no_of_pages):
       self.name=name
       self.price=price
       self.author_name=author_name
       self.author_born=author_born
       self.publishing_year=2020
       self.no_of_pages=no_of_pages
       StoryBook.no_of_books+=1

    def get_book_info(self):
        print(f'The book name:{self.name},price:{self.price}')
    def get_author_info(self):
        print(f'author name is:{self.author_name},author born in:{self.author_born}')

    #appling discount to an instance
    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)

class Library:
    def __init__(self,book_list=None):
        if book_list is None:
            self.book_list=[]
        else:
            self.book_list=book_list  

    def get_all_books(self):
        for book in self.book_list:
            print(f'Title:{book.name},Author:{book.author_name},price:{book.price}')
    def add_book(self,book):
        self.book_list.append(book)
    def remove_book(self,book):
        self.book_list.remove(book)


book_1=StoryBook('hamlet',400,'shakespeare',1990,2020,409)
book_2=StoryBook('the_kite_runner',300,'kaled',1996,202,3089)


public_library=Library()
public_library.add_book(book_1)
public_library.add_book(book_2)
public_library.get_all_books()
public_library.remove_book(book_2)
public_library.get_all_books()