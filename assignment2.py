def ascii_val_assignment(s):
    ascii_val = []
    updated = []
    for i in s:
        ascii_val.append(ord(i))
    print(ascii_val)
    for i in range(len(ascii_val)):
        if ascii_val[i] % 2 == 0 and i!=len(ascii_val)-1:
            if i+1 not in updated:
                updated.append(i+1)
                val = ascii_val[i] % 7
                if ascii_val[i+1] + val > 126 or ascii_val[i+1] + val < 33  :
                    ascii_val[i+1] = 83
                else:
                    ascii_val[i+1] = ascii_val[i+1] + val
        else:
            if i!= 0:
                if i-1 not in updated:
                    updated.append(i-1)
                    val = ascii_val[i] % 5
                    if ascii_val[i-1] + val > 126 or ascii_val[i-1] + val < 33  :
                        ascii_val[i-1] = 83
                    else:
                        ascii_val[i-1] = ascii_val[i-1] - val
    print(ascii_val)                    
    k = ''                    
    for i in ascii_val:
        k = k + chr(i)
    return k
                        
s = "sHQen}"   
z = ascii_val_assignment(s)
print(z)
    
'''output
[115, 72, 81, 101, 110, 125]
[115, 69, 83, 101, 107, 83]
sESekS
'''

        










