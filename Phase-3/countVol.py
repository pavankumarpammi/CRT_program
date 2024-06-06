def countVol(s,n):
    if n<0:
        return ''
    if s[n] in 'aeiou': 
        return s[n]+countVol(s,n-1)
    return countVol(s,n-1)
s=input().lower()
print(countVol(s,len(s)-1))
    
