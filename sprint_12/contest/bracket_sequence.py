def is_correct_bracket_seq(sequence: str) -> bool:
    if len(sequence) == 0:
        return True

    if len(sequence) % 2 != 0:
        return False
    stack_seq = []
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    for bracket in sequence:
        if bracket in open_brackets:
            stack_seq.append(bracket)
        elif bracket in close_brackets:
            if len(stack_seq) == 0:
                return False
            cur = stack_seq[-1]
            idx = close_brackets.index(bracket)
            if cur != open_brackets[idx]:
                return False
            stack_seq.pop()

    return True


def main() -> None:
    seq = str(input())
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()
