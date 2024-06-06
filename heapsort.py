import pygame

def heapify(arr, n, i):
    """
    Ensure the subtree rooted at index i is a max-heap.

    :param arr: List of elements
    :param n: Size of the heap
    :param i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root
        heapify(arr, n, largest)

def build_heap(arr):
    """
    Build a max-heap from an unsorted array.

    :param arr: List of elements
    """
    n = len(arr)  # Get the total number of elements in the array
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    Perform heap sort on a list of elements.

    :param arr: List of elements to be sorted
    """
    n = len(arr)  # Get the total number of elements in the array

    # Build a max-heap
    build_heap(arr)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
if __name__ == "__main__":

    pygame.init()

    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)

    pygame.quit()