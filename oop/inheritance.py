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


housebot=HouseBot('Bob',1.1,50)

print(housebot.name)
print(housebot.version)

housebot.move_forward()
housebot.moving_right()
housebot.clean()
housebot.clean()
housebot.clean()
print(housebot.area_covered)
housebot.set_cover_area(50)
housebot.clean()


