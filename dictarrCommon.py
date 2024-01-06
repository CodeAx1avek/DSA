from collections import Counter
ar1 = [1, 5, 3, 20, 40, 80]
ar2 = [3, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


def commonElement(ar1, ar2, ar3):
    arr1 = Counter(ar1)
    arr2 = Counter(ar2)
    arr3 = Counter(ar3)
    common = []
    dicResult = dict(arr1.items() & arr2.items() & arr3.items())

    for (key,value) in dicResult.items():
        for i in range(0,value):
            common.append(key)
    return common
print(commonElement(ar1,ar2,ar3))