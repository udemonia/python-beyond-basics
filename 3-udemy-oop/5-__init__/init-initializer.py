# What if we want some attributes to be created before the creation of an instance?

# this can be done in the constructor 

#?  __init__() -> private, used before the creator of the object - not called by the user
#?  Called Magic Method because its called automatically

class MagicMethods(object):
    def __init__(self, value):
        print('Calling __init__')
        # we want to validate data that goes into our data - validate before initialization
        #? Examples
            # Server - Validate we can connect to the server
            # Networking - Validate Connection
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value

    def inrimental(self):
        self.value += 1

mm = MagicMethods(25)
mm.inrimental()
mm.inrimental()

print(mm.value)