def merge(arr, left, mid, right):
    # Create temporary arrays
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Recursively sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)