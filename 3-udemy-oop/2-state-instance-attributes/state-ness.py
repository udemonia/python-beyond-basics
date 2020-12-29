class Joe(object):
    greeting = 'Hello, Joe'

thisjoe = Joe()

print(thisjoe.greeting)

# variables defined to the class are available to the instance


class Brandon(object):
    def call_me(self):
        print('Calling the "Call Me" method from the base class')
        print(self) # <__main__.Brandon object at 0x7fc142dbf160>

this_brandon = Brandon()

this_brandon.call_me()

print(this_brandon) # <__main__.Brandon object at 0x7fc142dbf160>

# instance methods are called bound methods - 
# a method on an instance passes the instance as the first argument to the method (named self in the method)
 
 #! Since we know the instance is going to be passed first, we always notate it w/ self
    #! a common convention we need to follow

