
# The Classic Example in Academia - The Instance Counter

class InstanceCounter(object):
    count = 0
    #class data is data that will be shared among instances

    def __init__(self, value):
        self.value = value
        InstanceCounter.count += 1 # accessing a class value inside of the instance object.attribute notation
    
    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(3)
b = InstanceCounter(10)
c = InstanceCounter(19)

for obj in (a,b,c):
    print(f"The Value is {obj.get_value()}")
    print(f"The Count of is {obj.get_count()}")
    # We're looking in the instance for the count attribute in the get count method
    # We could also look at the object instance obj.count


# The Value is 3
# The Count of is 3
# The Value is 10
# The Count of is 3
# The Value is 19
# The Count of is 3