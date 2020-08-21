from string import ascii_uppercase, ascii_lowercase

def rot13(message):
    result=[]
    for l in message:
        i = 0
        if l.islower():
            i = ascii_lowercase.index(l)
            if i < 13:
                i += 13
                
            else:
                i -= 13
            result.append(ascii_lowercase[i])
            
        elif l.isupper():
            i = ascii_uppercase.index(l)
            if i < 13:
                i += 13
            else:
                i -= 13
            result.append(ascii_uppercase[i])
        else:
            result.append(l)
            
    return "".join(result)
