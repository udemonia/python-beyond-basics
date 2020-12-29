
class MaxSizeList(object):

    def __init__(self, max_size):
        #take max size as an argument on instance creation
        # create empty list upon initialization
        self.max_size = max_size
        self.maxed_list = []

    def push(self, item):
        # no matter what, we append item
        self.maxed_list.append(item)
        if len(self.maxed_list) > self.max_size:
            self.maxed_list.pop(0)

    def get_list(self):
        return self.maxed_list
if __name__ == '__main__':
    a = MaxSizeList(3)

    a.push('Hello')
    a.push('Brae')
    a.push('is')
    a.push('a GIRL')

    print(a.get_list())