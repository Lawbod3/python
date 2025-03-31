from zipfile import sizeEndCentDir


class My_queue:
      def __init__(self, size):
      self.__queue = [None] * size

      def __len__(self):
          return len(self.__queue)

      def isEmpty(self):
          return len(self.__queue) == 0

      def put(self, item):
          self.__queue.append(item)

      def dequeue(self):
          if len(self.__queue) == 0:
              return None
          return self.__queue.pop(0)





