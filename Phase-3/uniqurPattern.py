def possiblString(i,n,s):
    if i==n:
        print(s)
        return ''
    possiblString(i+1,n,s+'0')
    possiblString(i+1,n,s+'1')
possiblString(0,4,'')
