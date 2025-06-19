def second_largest_sort(arr):
    unique_arr = list(set(arr))  
    if len(unique_arr) < 2:
        return None  
    unique_arr.sort(reverse=True)
    return unique_arr[1]

arr = [10, 20, 4, 45, 99, 99, 45]
print("Second largest (with sort):", second_largest_sort(arr))
