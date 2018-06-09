
def no_of_vow(string):
    vow = 'aeiou'
    count = 0
    for c in string:
        if c in vow:
            count += 1
    return count

def no_of_vow2(string):
    return sum([1 if c in 'aeiou' else 0 for c in string])
   

str2=raw_input("enter a string")
res = no_of_vow(str2)
print("the no of vowels:",res)
