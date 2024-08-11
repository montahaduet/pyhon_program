class Dancer:
    def __init__(self,style):
        self.style=style

    def dance(self):
        print(f'Dancing in {self.style}')  

class Singer:
    def __init__(self,genere):
        self.genere=genere

    def sing(self):
        print(f'Singing{self.genere} music')

class Artist:
    def __init__(self,painting_material):
        self.painting_material=painting_material
    def paint(self):
        print(f'painting with {self.painting_material}')

class SupperHumun(Dancer,Singer,Artist):
    def __init__(self,style,genere,painting_material,sports):
        Dancer.__init__(self,style)
        Singer.__init__(self,genere)
        Artist.__init__(self,painting_material)
        self.sports=sports
    def   play_sport(self):
        print(f'Playing {self.sports}')

    # overriding the Dance method of Dancer class
    def dance(self):
        print(f'Dancing with my own {self.sports}')


s=SupperHumun('Hip-Hop','Classical','Acraylic','football')
print(s.style)
print(s.genere)
print(s.painting_material)
print(s.sports)
s.dance()
s.sing()
s.paint()
s.play_sport()


