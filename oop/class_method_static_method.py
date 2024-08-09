
class StoryBook:
    no_of_books=0
    discount=0.5



    def __init__(self,name,price,author_name,author_born,publishing_year,no_of_pages):
       self.name=name
       self.price=price
       self.author_name=author_name
       self.author_born=author_born
       self.publishing_year=publishing_year
       self.no_of_pages=no_of_pages
       StoryBook.no_of_books+=1

    def get_book_info(self):
        print(f'The book name:{self.name},price:{self.price},pages:{self.no_of_pages}')
    def get_author_info(self):
        print(f'author name is:{self.author_name},author born in:{self.author_born}')

    #appling discount to an instance
    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)

    # method to change price
    def set_price(self,new_price):
        self.price=new_price

    #class method 1
    @classmethod
    def set_discount(cls,new_discount):
        cls.discount=new_discount
    #class method 2
    @classmethod
    def construct_from_string(cls,book_str):
        name, price, author_name, author_born,publishing_year,no_of_pages=book_str.split(',') 

        return cls(name, price, author_name, author_born, publishing_year, no_of_pages)

    #static method
    @staticmethod
    def is_new(publishing_year):
        if publishing_year>2016:
            print('yes it is a new book!')
        else:
            print('no it is not a new book!')    

book_1=StoryBook('hamlet',400,'shakespeare',1990,2020,409)
book_2=StoryBook('the_kite_runner',300,'kaled',1996,202,3089)

#for class method 1 output
# print(book_1.price)
# print(book_1.discount)
# StoryBook.set_discount(0.6)
# book_1.apply_discount()
# print(book_1.price)

book_str='harry_poter,200,jk roling,1970, 2020,400'
harry_poter=StoryBook.construct_from_string(book_str)
StoryBook.is_new(book_1.publishing_year)
print(harry_poter.name)