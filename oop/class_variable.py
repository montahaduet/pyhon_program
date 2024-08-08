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

book_1=StoryBook('hamlet',400,'shakespeare',1990,2020,409)
book_2=StoryBook('the_kite_runner',300,'kaled',1996,202,3089)


print(book_1.no_of_books)
print(book_2.no_of_books)
print(StoryBook.no_of_books)


print(book_2.price)
book_2.apply_discount()
print(book_2.price)