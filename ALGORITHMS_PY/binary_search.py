def binary_search(a,k):
    low=0
    high= len(a)-1
    a= sorted(a)
    mid=0
    while low<=high:
        mid= low+ (high-low)//2
        if a[mid] > k:
            low=mid+1
        elif a[mid] <k:
            high=mid-1
        elif a[mid] ==k:
            print (mid)
            return mid
    return -1

if __name__ == '__main__':
    a= [1,2,3,1,3,5]
    k=2
    result = binary_search(a,k)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")