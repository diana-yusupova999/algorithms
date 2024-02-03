def correct_bracket_sequence(n: int, result: str, count: int):
    if count < 0:
        return result
    if n == 0:
        if result is not None and count == 0:
            print(result)
        return result

    correct_bracket_sequence(n - 1, result + '(', count + 1)
    correct_bracket_sequence(n - 1, result + ')', count - 1)


if __name__ == '__main__':
    n = int(input())
    correct_bracket_sequence(n * 2, '', 0)
