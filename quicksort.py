def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1  # Number of elements in the left partition

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i - k)

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        raise IndexError("k is out of bounds.")
    return quickselect(arr.copy(), 0, len(arr) - 1, k)

def find_kth_largest(arr, k):
    if k < 1 or k > len(arr):
        raise IndexError("k is out of bounds.")
    return quickselect(arr.copy(), 0, len(arr) - 1, len(arr) - k + 1)

# Example usage:
arr = [3, 2, 1, 5, 4]
k_smallest = 3  # Find the 3rd smallest element
k_largest = 2   # Find the 2nd largest element

ith_smallest = find_kth_smallest(arr, k_smallest)
ith_largest = find_kth_largest(arr, k_largest)

print(f"The {k_smallest}rd smallest element is {ith_smallest}")
print(f"The {k_largest}nd largest element is {ith_largest}")
