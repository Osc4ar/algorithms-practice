def insertion_sort(arr: list[int]):
    # we skip 0 position since a one element array is already sorted
    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1

    return arr

arr = [10, 4, 1, 11, 0]
print(f'Unsorted array {arr}')

print(f'Sorted array {insertion_sort(arr)}')
