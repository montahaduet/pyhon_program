class Toy:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def sort_priority(self): 
        return self.price
    
def print_toy_object(toy_list):
    for obj in toy_list:
        print(f'Toy:{obj.name},Price:{obj.price}')

toy_1=Toy('Woody',1000)
toy_2=Toy('a',24)
tot_3=Toy('c',381)

#lambda
toys_again=[toy_1,toy_2,tot_3]

#using the lambda function with sort()

toys_again.sort(key=lambda x:x.price)
print_toy_object(toys_again)

# using the lamda function with sorted()

sorted_toys_again=sorted(toys_again,key=lambda x:x.price )
print_toy_object(sorted_toys_again)