import sys


class StackMaxEffective:
    def __init__(self):
        self.items: list = []
        self.__max_item: int = 0

    def push(self, val):
        if len(self.items) == 0:
            self.__max_item = val
        else:
            self.__max_item = self.items[-1][-1]
            if val > self.__max_item:
                self.__max_item = val

        self.items.append([val, self.__max_item])

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        else:
            print(self.items[-1][-1])


def main() -> None:
    stack = StackMaxEffective()
    num_command = int(input())
    for i in range(num_command):
        command = sys.stdin.readline().rstrip()
        if command == 'get_max':
            stack.get_max()
            continue

        if command == 'pop':
            stack.pop()
            continue

        command, val = command.split(' ')
        if command == 'push':
            stack.push(int(val))


if __name__ == '__main__':
    main()
