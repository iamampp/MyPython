# ���󹤳������ṩ�ӿ�ʹ�ã������õ���������ʵ���࣬�������£����õ���dog��cat��Ϳ���ʹ�����ǵķ���
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