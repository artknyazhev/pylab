# Array
# nums = []
# nums.insert(0,10)
# nums[5] = -1
# nums.insert(-len(nums),8)
# nums.insert(len(nums),8)
# nums.append([0])
# nums.append([0,1])
# nums.append([0,1,2])
# nums.append([0,1,2,3])
# del(nums[0])
# tmp = [0]
# for i in range(10):
#     nums.append(tmp)
#     tmp.insert(len(tmp),tmp[len(tmp)-1]+1)
#
# tmp.reverse()
#
# rzd = "\n-------"
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         print(nums[i][j],end = " | ")
#     print(rzd)
#     rzd += "----"
#
# print(nums.count([10,9,8,7,6,5,4,3,2,1,0]))
# print(nums.__len__())
import random
from random import randint


def findMin(arr) -> int:
    min = 0
    flag = True
    for i in range(len(arr)):
        if arr[i][2] == "A" and arr[min][0] > arr[i][0]:
            min = i
            flag = False
    if flag:
        for i in range(len(arr)):
            if arr[min][0] > arr[i][0]:
                min = i

    return min


def Check(money, arr) -> bool:
    flag = False
    for i in range(len(arr)):
        if arr[i][0] <= money:
            flag = True
    return flag


def PrintShop(arr):
    for i in range(len(arr)):
        print(arr[i], "\n")

# ---------------------------new bug fix--------------------------------

# -------------------------new branch----------------------------------

type = ["A", "B"]
shop = []
money = int(input("Введите кол-во денег: "))
_B = 0
for i in range(int(input("\nКол-во товаров: "))):
    shop.append([randint(10, 100), randint(1, 20), random.choice(type)])
flag = True
while flag or not shop:
    min = findMin(shop)
    for i in range(len(shop[min])):
        if shop[min][0] < money:
            if shop[min][1] != 0:
                if shop[min][2] == "B":
                    _B += 1
                money -= shop[min][0]
                shop[min][1] -= 1
            else:
                del (shop[min])
                break
    flag = Check(money, shop)
    PrintShop(shop)
    print("Money: ", money, "$")

print("Товаров 'B' куплено: ", _B, "\nДенег осталось: ", money, "$")
#hello artknyazhev
