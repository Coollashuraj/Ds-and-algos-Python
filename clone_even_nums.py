def clone_even(a):
    end = len(a) -1
    print(end)
    # find last element index
    index= find_last(a)

    """if even , copy twice to length pointer
      #copy once and decrement lengthpointer"""
    while(index > 0):
        if a[index] %2 ==0:
            a[end] =  a[index]
            end -=1
        a[end] =  a[index]
        end -=1
        index -=1
    print(a)
    return a

def find_last(a):
    i= len(a)-1
    while (i>=0 and a[i]==-1):
        i-=1
    return i

if __name__ == '__main__':
    clone_even([1,2,3,-1])