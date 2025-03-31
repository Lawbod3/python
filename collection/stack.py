class stack:
      def __init__(self):
          self.__stack = []

      def push(self, item):
          self.__stack.append(item)

      def pop(self):
          return self.__stack.pop(len(self.__stack) - 1)

      def clear(self):
          self.__stack = []

      def __str__(self):
          return str(self.__stack)

      def len(self):
          return len(self.__stack)

      def __getitem__(self, index):
          return self.__stack[index]

      def __setitem__(self, index, value):
          self.__stack[index] = value

      def remove(self, value):
          self.__stack.remove(value)

      def peek(self):
          return self.__stack[len(self.__stack) - 1]

      def isEmpty(self):
          if len(self.__stack) == 0:
              return True
          return False

