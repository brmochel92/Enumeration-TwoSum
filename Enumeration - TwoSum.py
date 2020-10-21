arr1 = [1, 3, 5, 6]
target1 = 8

def two_sum(array, target):
    values = dict()

    for i, number in enumerate(array):
        comp = target - number

        if comp in values:
            return [values[comp], i]

        values[number] = i
    return []

list1 = two_sum(arr1, target1)
print(list1)







