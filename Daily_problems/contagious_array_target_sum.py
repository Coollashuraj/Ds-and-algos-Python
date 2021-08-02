#Given an array of positive integers, find the contiguous subarray that sums to a given number X.

def subarray_sum(A,target):
    start=0
    end=0
    sum=A[0]
    while(start<len(A)):
        if sum< target:
            if end>len(A):
                break
            end+=1
            sum=sum+A[end]
        elif sum>target:
            sum -=A[start]
            start+=1
        else:

            return start, end
    return -1
if __name__ == '__main__':
    a,b=0,0
    a, b=  subarray_sum([1,2,3,1],5)
    print(a,b)