def reverse_list(arr):
    """Given an array of numbers, reverse the list."""
    # REMOVE BELOW FOR CLASS
    l = []
    for i in range(len(arr) - 1, -1, -1):
        l.append(arr[i])
    return l


if __name__ == '__main__':
    l= reverse_list([1,2,3,-1])
    print(l)