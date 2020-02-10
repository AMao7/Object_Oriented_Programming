from animal_class import Animal

class Reptile(Animal):      # subclass of animal
    pass

    def seek_heat(self):
        return 'where the sun at '

    def lay_eggs(self):
        return 'pop pop pop pop pop'

    def hibernate(self):
        return "bit chilly, think I'll just stop my heart for a second or two"




# ringo = Reptile('ringo', 4)
#
# print(type(ringo))
# print(ringo.name)
# print(ringo.eat(' burger'))