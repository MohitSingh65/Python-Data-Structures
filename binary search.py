def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l +  (r - l)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid -1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
xlist = input("Enter the sorted elements: ")
xlist = xlist.split()
xlist = [int(x) for x in xlist]

key = int(input("Enter the element to be searched: "))
result = binarySearch(xlist, 0, len(xlist)-1, key)

if result != -1:
    print("{} was found at index {}.".format(key, result))
else:
    print("{} was not found.".format(key))

