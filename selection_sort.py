def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print( selectionSort([5, 3, 6, 2, 10]) )

# findSmallest: index = 0, smallest = arr[0] = 5, len(arr) = 4, for 1 to 4
#    when i = 1, arr[1] = 3 < (smallest = 5), so smallest = 3 and index = 1
#    when i = 2, arr[2] = 6 not < (smallest = 3), next one
#    when i = 3, arr[3] = 2 < (smallest = 3), so smallest = 2 and index = 3
#    when i = 4, arr[4] = 10 not < (smallest = 3), end
#    return index = 3

# selectionSort: len(arr) = 4, for 0 to 4
#    when i = 0, get smallest_index = 3, pop arr[3] and append into newArr
#        newArr = [2]; arr = [5, 3, 6, 10]
#    when i = 1, get smallest_index = 2, pop arr[2] and append into newArr
#        newArr = [2, 3]; arr = [5, 6, 10]
#    when i = 2, get smallest_index = 0, pop arr[0] and append into newArr
#        newArr = [2, 3, 5], arr = [6. 10]
#    when i = 3, get smallest_index = 0, pop arr[0] and append into newArr
#        newArr = [2, 3, 5, 6], arr = [10]
#    when i = 4, get smallest_index = 0, pop arr[0] and append into newArr
#        newArr = [2, 3, 5, 6, 10], arr = []