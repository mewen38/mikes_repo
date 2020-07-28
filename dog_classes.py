# I remember feeling very uncomfortable with classes, so I'm forcing myself to mess around after reading an article

class animal:
    def __init__ (self, name, color, type):
        self.animal_name = name
        self.animal_color = color
        self.animal_type = type
    def speak(self):
        print('happy thoughts, happy thoughts, boy im getting mighty sick of this')

    def dance(self):
        print('{} does an animal class wiggle'.format(self.animal_name))


class dog(animal):
    def __init__ (self, name, color, type, special_dance):
        super().__init__ (name, color, type)
        self.dog_special_dance = special_dance
    
    def speak(self):
        print('woof woof, bow-wow')

    def dance(self):
        print('{}, as a dog, knows a special overriding animal subclass (dog) {} wiggle'.format(self.animal_name, self.dog_special_dance))
        
class cat(animal):
    def speak(self):
        print("the toppings contain potassium benzoate .................. that's bad")

class princess(animal):
    def __init__ (self, name, color, type, area_of_expertise):
        super().__init__ (name, color, type)
        self.princess_area_of_expertise = area_of_expertise

    def speak(self):
        print("i wrote this program, im a princess, and i love kibble")

bailey = animal('bailey','red', 'red mage dog')
weezer = dog('weezer','grey', 'wizard dog', 'spicy bachata')
zelda = princess('zelda', 'red', 'princess', 'java, python, react, go, npm, pyenv, aws, airflow, sql, redshift, s3, s3 glacier, spark, kibble')
pepper = cat('pepper', 'black', 'cat')


print(bailey,bailey.animal_name, bailey.animal_type)
bailey.speak()
bailey.dance()

print(weezer, weezer.animal_name, weezer.animal_type)
weezer.speak()
weezer.dance()

print(zelda, zelda.animal_name, zelda.animal_color, zelda.animal_type, zelda.princess_area_of_expertise)
zelda.speak()

print(pepper, pepper.animal_name, pepper.animal_color, pepper.animal_type)
pepper.speak()