
#! instance attribute data

import random

class MyClass(object):
    def doThis(self):
        print('Doing This: ')
        self.rand_value = random.randint(1,10)
        # we call the attribute of an instance the 'state' of an instance
        print(self.rand_value)

my_instance = MyClass()

my_instance.doThis()
my_instance.rand_value


#* in this example - what is self - SELF is the object on which the method was called - 
#? self is the instance upon which the method was called!

