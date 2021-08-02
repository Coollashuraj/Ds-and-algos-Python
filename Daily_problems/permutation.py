def permutation(str):
    result= ""
    return permutation_rec(result,str)

def permutation_rec(result,str):

    #Base case
    n=len(str)
    if n==0:
        print(result)
    else:
        for i in range(n):
            #print(result+str[i])
            permutation_rec(result+str[i],str[0:i]+str[i+1:n])

if __name__ == '__main__':
    l= permutation("mln")
    #print(l)