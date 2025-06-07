def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

lst = list(map(int, input("Enter list with possible duplicates: ").split()))
print("List without duplicates:", remove_duplicates(lst))
