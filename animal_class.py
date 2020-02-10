class Animal():
    # characteristics - attributes
    def __init__(self, name, legs):     # initiates a method which is a function wrapped in a class

        self.name = name
        self.legs = legs

    def eat(self, food = ''):       # makes the argument optional
            return 'nom nom nom nom' + food

    def sleep(self):
            return "zzzzz"

    def potty(self):
            return ' 0_0 ....... HMMMMMMMMMMMM O_o...SPLOSH'

    def hunt(self):
        return 'Attacccccckkkkk!!!!!'

        # behaviours
        # methods - which are like functions that belong to a class
        # will be called onto objects of that class




# let's create an instance of an animal object (by assigning it to a variable)

# animal_1 = Animal('Randy Marsh','many')
# animal_2 = Animal('Cartman', 'a lot',)
# print(animal_1)
#
# # checking attributes
# print(animal_1.name)       # can get out the information of the one individual item
# print(animal_2.name)
#
#
#
# # call methods on objects of class animal
#
# print(animal_1.eat())
#
#
# print(animal_2.eat())
