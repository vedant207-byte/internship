def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Reversed list:", reverse_list(lst))
