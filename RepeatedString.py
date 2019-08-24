def repeatedString(s, n):
    c=0
    for i in range(n):
        s=s+s
        if len(s)>=n:
            break
    for i in range(0,n):
        if(s[i]=='a'):
            c+=1
    return(c)
