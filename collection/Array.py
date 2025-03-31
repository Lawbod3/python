class Array:
    def __init__(self,size):
        self.__array = [None] * size


    def __len__(self):
        count = 0
        for num in self:
            count += 1
        return count

    def __getitem__(self, index):
        if index < 0 or index >= len(self.__array):
            raise IndexError('Index out of range')
        else:
            return self.__array[index]

    def get(self):
        return self.__array

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.__array):
            raise IndexError('Index out of range')
        else:
            self.__array[index] = value

    def iterable_array(self):
        for item in [self[num] for num in range(len(self))]:
            yield item

    def __str__(self):
        return str([self[num] for num in range(len(self))])

    def _fill(self,value):
        for num in range(len(self)):
            self[num] = value

    def contains(self,value):
        return value in self

    def copy_of_array(self,value):
        new_array =Array(value)
        for num in range(value):
            if num < len(self):
                new_array[num]= self[num]
        return new_array




