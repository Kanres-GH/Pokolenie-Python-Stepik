# объявление функции
def merge(list1, list2):
    numbers1.extend(numbers2)
    numbers1.sort()
    return numbers1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))