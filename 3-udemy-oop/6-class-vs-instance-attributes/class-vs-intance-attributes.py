


class YouTube(object):
    classy = 10 # Class variable 

    def set_value(self):
        self.insty= 100 #instance variable

mm = YouTube()
mm.set_value()

print(mm.insty) #  -> 10
print(mm.classy) # -> 100


class ClassAt(object):
    class_attribute = 'This is a class attribute'

dd = ClassAt()
print(dd.class_attribute) # -> This is a class attribute
dd.class_attribute = 'Fake Instance Attribute'
print(dd.class_attribute) # -> Fake Instance Attribute
del dd.class_attribute
print(dd.class_attribute) # -> This is a class attribute

# we can delete the class attribute that we defined outside of the class and preserve the class attribute value 

