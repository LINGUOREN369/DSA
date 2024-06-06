def partition(arr, low, high):
    """
    Partition the array using the first element as pivot.
    
    :param arr: List of elements
    :param low: Starting index
    :param high: Ending index
    :return: Index of the pivot element after partition
    """
    pivot = arr[low]  # Choose the first element as pivot
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort(arr, low, high):
    """
    Perform Quick Sort on the array.
    
    :param arr: List of elements
    :param low: Starting index
    :param high: Ending index
    """
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        print(f"Array after pivot {arr[pi]} placed at index {pi}: {arr}")

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage
if __name__ == "__main__":
    arr = [10,16,8,12,15, 6, 3, 9, 5]
    n = len(arr)
    print("Original array:", arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)