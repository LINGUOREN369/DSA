def IterativeBinarySearch(arr, n, key):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        if arr[mid] == key:
            return mid
        
        if mid < key:
            low = mid + 1

        if mid > key:
            high = mid - 1

    return -1

def RecursiveBinarySearch(A, low, high, key):

    mid = (low + high) // 2

    if low > high:
        return None
    
    if key == A[mid]:
        return mid
    
    if key > A[mid]:
       return RecursiveBinarySearch(A, mid+1, high, key)
    
    else:
        return RecursiveBinarySearch(A, low, mid-1, key)

A = [1,3,2,3,4,5]
print(RecursiveBinarySearch(A, 0, len(A)-1, 1))

        
