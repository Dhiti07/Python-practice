# Removing a character from a string

def remove_char(s1,ch):
    if(len(s1)==0 or s1 == ''):
        return s1
    small_answer = remove_char(s1[1:],ch)
    if(s1[0]==ch):
        return small_answer
    else:
        return s1[0]+small_answer
    
s1 = "good morningzzz"
ans = remove_char(s1,'z')
print(ans)

