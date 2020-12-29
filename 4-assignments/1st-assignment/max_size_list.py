
class MaxSizeList(object):
    # class attribute 
    #! This turned out to be wrong - it worked but broke encapsulation - 
    #! we want the list associated with the instance - only changing the instance not the class

    maxed_list = []
    
    def __init__(self, max_size):
        #take max size as an argument on instance creation
        self.max_size = max_size

    def push(self, item):
        # no matter what, we append item
        MaxSizeList.maxed_list.append(item)

        # check size
        if len(MaxSizeList.maxed_list) > self.max_size:
            MaxSizeList.maxed_list.pop(0)

    def get_list(self):
        return MaxSizeList.maxed_list


a = MaxSizeList(3)

a.push('Hello')
a.push('Brae')
a.push('is')
a.push('a GIRL')

print(a.get_list())