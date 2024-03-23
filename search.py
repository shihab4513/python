def search_item(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1
numbers = [10, 20, 30, 40, 50]
print(search_item(numbers, 30))  # Output: 2
print(search_item(numbers, 60))  # Output: -1
