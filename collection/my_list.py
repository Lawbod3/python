class my_list:
    def __init__(self, temp_size = 10):
        self.__elements = [None] * temp_size
        self.__size = 0


    def len(self):
        count = 0
        for num in self.__elements:
            if num is not None:
               count += 1
        return count


    def __resize(self):
        new_capacity = len(self.__elements) * 2
        new_elements = [None] * new_capacity
        for num in range(len(self.__elements)):
            new_elements[num] = self.__elements[num]
        self.__elements = new_elements

    def get(self):
        return self.__elements

    def __iter__(self):
        for num in self.__elements:
            yield num



    def __setitem__(self, index,  value):
        self.__elements[index] = value

    def append(self, value):
        if self.__size == len(self.__elements):
            self.__resize()
        self.__elements[self.__size] = value
        self.__size += 1

    def remove(self, value):
        self.__elements.remove(value)

    def get(self):
        return self.__elements


    def __str__(self):
        answer = []
        for num in self.__elements:
            if num is not None:
                answer.append(num)
        return str(answer)

    def extend(self, other):
        for num in other:
            if num is not None:
                self.__elements.append(num)
        return self.__elements

    def clear(self):
        self.__elements = []






