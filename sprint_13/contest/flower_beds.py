
def flowers_beds(flowerbed_coordinate: list, gardener: int) -> list:
    flowerbed_coordinate.sort()
    new_flowerbed_coordinate = []
    for i in range(gardener - 1):
        if flowerbed_coordinate[i][1] == flowerbed_coordinate[i + 1][0]:
            new_flowerbed_coordinate.append([flowerbed_coordinate[i][0], flowerbed_coordinate[i + 1][1]])


if __name__ == '__main__':
    gardener = int(input())
    flowerbed_coordinate = []
    for i in range(gardener):
        tmp = input().split(' ')
        flowerbed_coordinate.append([int(tmp[0]), int(tmp[1])])

    print(flowers_beds(flowerbed_coordinate, gardener))
