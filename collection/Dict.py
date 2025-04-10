from tkinter.constants import RAISED


class Dict:
    def __init__(self, **kwargs):
        self.__my_data = kwargs


    def isEmpty(self):
        if len(self.__my_data) == 0:
            return True
        return False

    def __setkey__(self, key, defualt=None):
        return self.__my_data.__setitem__(key, defualt)

    def set(self, key, value):
        if key in self.__my_data:
            raise KeyError("KEY already exists")
        else:
            self.__my_data[key] = value


