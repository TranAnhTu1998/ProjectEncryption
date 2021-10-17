import math
import random


def isEven(a):
    return a % 2 == 0


source_string = "ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИ"

length_source_string = len(source_string)

if not isEven(length_source_string):
    length_source_string += 1

print("len = ", length_source_string)
# Matrix 2m * 2n
mx2 = math.floor(math.sqrt(length_source_string))
print("m = ", mx2)
if not isEven(mx2):
    mx2 -= 1
print("mx2 lan 2 = ", mx2)
print("ength_source_string % m != 0 ", length_source_string % mx2 != 0)
while not (mx2 == 0 or (length_source_string % mx2 == 0 and isEven(length_source_string / mx2))):
    mx2 -= 2
    print("mx2 -= 2 ", mx2)

print('mx2 lan 3 = ', mx2)

if mx2 == 0:
    mx2 = 1

nx2 = int(length_source_string / mx2)

print("mx2 = ", mx2, "nx2 = ", nx2)

m = int(mx2 / 2)
n = int(nx2 / 2)

arr_binary_string = [[]]
for i in range(mx2):
    arr_binary_string[0].append([])
    for j in range(nx2):
        arr_binary_string[0][i].append(0)

print(len(arr_binary_string))
print(len(arr_binary_string[0]))
# Thiết lập mảng xoay mảng.
# Bảng 1
for cell in range(n * m):
    i = random.randint(0, mx2 - 1)
    j = random.randint(0, nx2 - 1)

    #Tìm vị trí thích hợp trong ma trận đáng dấu, sao thỏa mãn điều kiện dưới đâu để khi ta lấy đối xứng 4 lần thì ứng với mỗi ô (cell) không trùng lên cell khác.
    while arr_binary_string[0][i][j] == 1 or arr_binary_string[0][i][nx2 - 1 - j] == 1 or \
            arr_binary_string[0][mx2 - 1 - i][nx2 - 1 - j] == 1 or arr_binary_string[0][mx2 - 1 - i][j] == 1:
        i = random.randint(0, mx2 - 1)
        j = random.randint(0, nx2 - 1)
    arr_binary_string[0][i][j] = 1
print("arr_binary_string1 = ", arr_binary_string[0])

# print(len(arr_binary_string1), len(arr_binary_string1[0]))
# print(arr_binary_string1)

# Bảng 2
arr_binary_string.append([])
# print("arr_binary_string2 = ", arr_binary_string2)
for i in range(mx2):
    arr_binary_string[1].append([])
    for j in range(nx2):
        arr_binary_string[1][i].append(arr_binary_string[0][i][nx2 - 1 - j])
print("arr_binary_string2 = ", arr_binary_string[1])

# Bảng 3
arr_binary_string.append([])
# print("arr_binary_string3 = ", arr_binary_string[2])
for i in range(mx2):
    arr_binary_string[2].append([])
    for j in range(nx2):
        arr_binary_string[2][i].append(arr_binary_string[1][mx2 - 1 - i][j])
print("arr_binary_string3 = ", arr_binary_string[2])

# Bảng 4
arr_binary_string.append([])
# print("arr_binary_string4 = ", arr_binary_string4)
for i in range(mx2):
    arr_binary_string[3].append([])
    for j in range(nx2):
        arr_binary_string[3][i].append(arr_binary_string[2][i][nx2 - 1 - j])
print("arr_binary_string4 = ", arr_binary_string[3])

v = 0
arr_rota_lattice = []
for i in range(mx2):
    arr_rota_lattice.append([])
    for j in range(nx2):
        arr_rota_lattice[i].append(' ')


for k in range(4):
    for i in range(mx2):
        for j in range(nx2):
            if v == len(source_string):
                break
            if arr_binary_string[k][i][j] == 1:
                arr_rota_lattice[i][j] = source_string[v]
                v += 1
        if v == len(source_string):
            break
    if v == len(source_string):
        break

str_rota_lattice = ""
for i in range(mx2):
    for j in range(nx2):
        str_rota_lattice += arr_rota_lattice[i][j]

print("Закодирование")
print("Открытый тескт : ", source_string)
print('Шифрованный тескт :', str_rota_lattice)

print("Декодирование")
print("Открытый тескт : ", str_rota_lattice)
print('Шифрованный тескт :', source_string)
