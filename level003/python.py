numbers = [4, 8, 15, 16, 23, 42]

for i in range(len(numbers)):
    print(f"ინდექსი {i}: {numbers[i]}")





prices = [10, 25, 7, 40]

for i in range(len(prices)):
    prices[i] = prices[i] * 2

print(prices)








temps = [12, 15, 14, 18, 20, 19, 22]

count = 0

for i in range(len(temps) - 1):
    if temps[i + 1] > temps[i]:
        print("ტემპერატურა გაიზარდა")
        count += 1
    elif temps[i + 1] < temps[i]:
        print("ტემპერატურა შემცირდა")
    else:
        print("ტემპერატურა არ შეცვლილა")

print("ტემპერატურა გაიზარდა", count, "ჯერ")








