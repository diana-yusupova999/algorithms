# ID 88612894
import sys


class DeQueError(Exception):
    pass


class DeQueSized:
    def __init__(self, max_size: int):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__size = 0
        self.__head = 0
        self.__tail = 1

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__max_size

    def push_back(self, x) -> None:
        if self.is_full():
            raise DeQueError

        self.__items[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, x) -> None:
        if self.is_full():
            raise DeQueError
        self.__items[self.__head] = x
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise DeQueError

        self.__tail = (self.__tail - 1) % self.__max_size
        val = self.__items[self.__tail]
        self.__items[self.__tail] = None
        self.__size -= 1
        return val

    def pop_front(self):
        if self.is_empty():
            raise DeQueError

        self.__head = (self.__head + 1) % self.__max_size
        val = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__size -= 1
        return val

    def get_size(self) -> int:
        return self.__size


def main() -> None:
    num_command = int(input())
    max_size_queue = int(input())
    queue = DeQueSized(max_size_queue)
    command = 'pop'

    for i in range(num_command):
        command, *val = sys.stdin.readline().rstrip().split(' ')
        try:
            method = getattr(queue, command)
            result = method(*val)
            if result is not None:
                print(result)
        except DeQueError:
            print('error')


if __name__ == '__main__':
    main()
