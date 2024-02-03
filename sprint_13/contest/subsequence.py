def subsequence_2(str_1, str_2):
    index_1 = 0
    for index_2 in range(len(str_2)):
        if str_1[index_1] == str_2[index_2]:
            if index_1 == len(str_1) - 1:
                return True
            index_1 += 1
    return False


if __name__ == '__main__':
    str_1 = input()
    str_2 = input()
    print(subsequence_2(str_1, str_2))
