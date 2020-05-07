# 抽象工厂可以提供接口使用，而不用调用他们真实的类，例如以下，不用调用dog和cat类就可以使用他们的方法
class PetShop():
    def __init__(self,pet):
        self.pet = pet
    def show_pet(self):
        print("we have a lovely pet {}".format(self.pet()))
        print("it says {}".format(self.pet().speak()))

class Dog():
    def speak(self):
        return "woof"
    def __str__(self):
        return 'Dog'

class Cat():
    def speak(self):
        return "meow"
    def __str__(self):
        return 'Cat'

dog = PetShop(Dog)
dog.show_pet()