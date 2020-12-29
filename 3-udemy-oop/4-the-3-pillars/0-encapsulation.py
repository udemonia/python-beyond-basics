
# we're taking in a value and setting it as a value in an instance


class MyClass(object):
    #* SETTER VALUE - common OOP term
    def set_value(self, val):
        self.value = val 
    #* GETTER VALUE - common OOP term
    def get_value(self):
        return self.value

a = MyClass()
b = MyClass()

a.set_value(10)
b.set_value(20)

print(a.get_value())
print(b.get_value())

#! - if we can just run a.value = 10 why build a method (setter method) to handle it???

#* - The answer is we're building a gateway to STATE - we're preserving the integrity of the instances attributes

#* encapsulating the instance

class MyInteger(object):
    def set_my_value(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_my_value(self):
        return self.val
    
    def increment_val(self, val):
        self.val += 1

i = MyInteger()
i.set_my_value(9)
print(i.get_my_value())
i.set_my_value('hi')
print(i.get_my_value())
