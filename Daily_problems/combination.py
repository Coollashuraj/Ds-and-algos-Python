def comb_aux_buffer(s):

    buffer=[None]*len(s)
    #res = [False] * len(s)
    return comb_rec(s,0,buffer,0)

def comb_rec(s,b_i,buffer,s_i):
    if b_i==len(buffer):
        print(buffer[:b_i])
        return
    for i in range(s_i,len(s)):
        buffer[b_i] = s[i]
        comb_rec(s, b_i+1, buffer,i)


if __name__ == '__main__':
    l= comb_aux_buffer("lmn")
