def permute_aux_buffer(s):

    buffer=[None]*len(s)
    res = [False] * len(s)
    return permute_rec(s,0,buffer,res)

def permute_rec(s,b_i,buffer,res):
    if b_i==len(buffer):
        print(buffer[:b_i])
        return
    for i in range(len(s)):
        if res[i] ==False:
            buffer[b_i] = s[i]
            res[i] = True
            permute_rec(s, b_i+1, buffer,res)
            res[i] = False

if __name__ == '__main__':
    l= permute_aux_buffer("lmnopn")
