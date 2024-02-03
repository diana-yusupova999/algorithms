# ID 88612406
import operator
from typing import Union


class StackEmptyError(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, x: Union[int, str]) -> None:
        self.items.append(x)
        self.size += 1

    def pop(self) -> Union[int, str]:
        if self.is_empty():
            raise StackEmptyError
        self.size -= 1
        return self.items.pop()


class Calculator:
    operator = {'+': operator.add, '-': operator.sub,
                '*': operator.mul, '/': operator.floordiv}

    def __init__(self, input_items: list):
        self.items: list = input_items

    def calculate(self) -> int:
        numbers = Stack()
        for item in self.items:
            if item in self.operator.keys():
                num_1 = numbers.pop()
                num_2 = numbers.pop()
                result = self.operator[item](num_2, num_1)
                numbers.push(result)
            else:
                numbers.push(int(item))
        return numbers.pop()


def main() -> None:
    input_items = input().split(' ')
    calc = Calculator(input_items)
    print(calc.calculate())


if __name__ == '__main__':
    main()
