
def buying_houses(sale, houses, budget) -> int:
    number = 0
    sale.sort()
    if sale[0] > budget:
        return number

    for i in range(houses):
        if sale[i] <= budget:
            number += 1
            budget = budget - sale[i]
    return number


if __name__ == '__main__':
    houses, budget = input().split(' ')
    sale = input().split(' ')
    for i in range(len(sale)):
        sale[i] = int(sale[i])

    print(buying_houses(sale, int(houses), int(budget)))
