



def is_palindrome(string):
    string.lower()
    string_sep = ''.join(c for 
                         c in string if 
                         c.isalpha())
    string_rev = string_sep[::-1]
    is_pal = string_sep == string_rev
    return is_pal

string_tab = input().split()
pal_tab = []

for el in string_tab:
    if is_palindrome(el) == True:
        pal_tab.append(el)
        
print(pal_tab)

