
def shortest_substring(s,x):
    substring = []

    for i in range (len(s)):
        temp = s[i]
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                temp = temp + s[j]
                break
            else:
                temp = temp + s[j]
                
        if (temp[-1] == s[i]) and len(temp) >= x and len(temp) < len(s):
            substring.append(temp)
        temp = ""
        
    if len(substring) == 0 :
        return ("not-found")
    else:
        min  = len(substring[0])
        for i in range(1,len(substring)):
            if len(substring[i]) < min :
                min = len(substring[i])
        k = ''
        for i in substring:
            if len(i) == min :
                k = k + i + ' '
        return k

# test 1
s ='abccdbacca'
for i in range (3,len(s)):
    x = i
    print (f"{i} = {shortest_substring(s,x)}")

'''output : 
3 = acca 
4 = acca 
5 = bccdb cdbac 
6 = abccdba 
7 = abccdba 
8 = not-found
9 = not-found'''