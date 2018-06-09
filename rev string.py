


def p(s):
    for i in range(lenth):
        if(s[i]!=s[lenth-1-i]):
            return False
    return True



print p(raw_input("enter a string:"))
