class Robot:
    def __init__(self,name,version):
        self.name=name
        self.version=version

    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving right! ')
    def moving_left(self):
        print(f'{self.name} is moving left! ')
    def moving_right(self):
        print(f'{self.name} is moving right! ')

class HouseBot(Robot):
    def __init__(self, name, version,area_covered):
        super().__init__(name, version)
        self.area_covered=area_covered

    def clean(self):
        if self.area_covered > 0:
            print(f'{self.name} is claning the house')
            self.area_covered -=30

            if self.area_covered < 0:
                self.area_covered = 0
        else:
            print('cannot clean! ,PLEASE reset the area_covered perameter')

    def set_cover_area(self,area):
        if self.area_covered==0:
            self.area_covered=area
        else:
            print('i can still clean more area')



    @staticmethod
    def halt():
        print('i am halting')

    #overriding the forward method

    def move_forward(self):
        print('this is an house bot class!')
        super().move_forward() 


class MaidBot(HouseBot):
    def __init__(self, name, version, area_covered,cooking):
        super().__init__(name, version, area_covered)
        self.cooking=cooking    
m=MaidBot('gantel',1.3,100,'cake')

print(m.cooking)

housebot=HouseBot('Bob',1.1,50)
robo=Robot('stan lee',1.5)

# print(help(Robot))
# print(help(list))

# print(help(housebot))

# print(issubclass(HouseBot,Robot))
# print(issubclass(Robot,HouseBot))
# print(issubclass(Robot,object))
# print(issubclass(HouseBot,object))

# print(isinstance(housebot,Robot))
# print(isinstance(housebot,HouseBot))
# print(isinstance(housebot,object))
# print(isinstance(robo,object))

