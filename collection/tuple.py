class my_tuple:
    def __init__(self, *input):
        self.__my_value = input
        self.__immutable_input = input

    def print__(self):
        return str(self.__immutable_input)


    def getvalue(self, index):
        return self.__immutable_input[index]

    def __getitem__(self, index):
        return self.__immutable_input[index]

    def __add__(self, other):
        if isinstance(other, my_tuple):
            return my_tuple(*self.__immutable_input, *other.__immutable_input)
        else:
            raise TypeError("can only add my_tuple")

    def length_my_tuple(self):
        return len(self.__immutable_input)

    def iterable_(self):
        for item in self.__immutable_input:
            yield item

    def contains_value(self, value):
        return value in self.__immutable_input










