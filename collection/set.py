class my_set:
    def __init__(self, *input):
        self.__elements = []
        for element in input:
            if element not in self.__elements:
                self.add(element)

    def __len__(self):
        count = 0
        for number in self.__elements:
            count += 1
        return count

    def __iter__(self):
        for num in self.__elements:
            yield num

    def add(self, value):
        self.__elements.append(value)

    def clear(self):
        self.__elements = []

    def remove(self, value):
        self.__elements.remove(value)

    def __contains__(self, value):
        return  value in self.__elements

    def __str__(self):
        return str(self.__elements)

