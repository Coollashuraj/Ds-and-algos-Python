#class my_sorted_list:

 def mergee_sort(lst):

    middle = len(lst) // 2
    left  = lst[:middle]
    right = lst[middle:]
    sleft= merge_sort(left)
    sright= merge_sort(right)
    return merge(sleft and sright)
 def merge(left, right):
    result =[]
    while(left and right):
     if left[0] < right[0]:
       result.append(left[0])
       left.pop(0)
     else :
       result.append(right[0])
       right.pop(0)
     if left:
        result +=left
    if right:
       result += right
    return result
 lji= [1,29,9,5]
can = mergee_sort(lji)
