def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        # overhead the item, item is in the left side
        elif guess > item:
            high = mid - 1
        # under the item, item is in the right side
        else:
            low = mid + 1
    return mid

my_list = [1,3,5,7,9]
print("position is: ", binary_search(my_list, 3))
print("position is: ", binary_search(my_list, 7))
print()
