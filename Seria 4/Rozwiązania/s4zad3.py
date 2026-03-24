


brackets = '([{{[]}}]())'
brackets2 = brackets

check = True
if check == True:

    brack_tab = ['[]','()','{}']
    
    
    is_ok = True
    while is_ok == True:
        len1 = len(brackets2)
        for brack in brack_tab:
            brackets2 = brackets2.replace(brack,'')
        
        len2 = len(brackets2)
        if len1 == len2:
            is_ok = False
            #return False
        #if len2 == 0:
            #return True
            
#%%
fix = True
if fix == True:
    
    brackets = '))((('
    brackets2 = brackets
    brach_tab = ['()']
    left_added = 0
    right_added = 0
    is_ok = True
    while is_ok == True:
        len1 = len(brackets2)
        for brack in brack_tab:
            brackets2 = brackets2.replace(brack,'')
        
        len2 = len(brackets2)
        if len1 == len2:
            brackets2 = '('+brackets2
            if '()' in brackets2:
                left_added += 1
            else:
                brackets2 = brackets2[1:]
                brackets2 = brackets2 +')'
                right_added += 1
        if len2 == 0:
            print(left_added, right_added)
            
            break

#%%
def brackets(what_to_do, arg2):
    
    if what_to_do == 'check' or what_to_do == 'fix':
        brackets = arg2
        brackets2 = brackets

    if what_to_do == 'check':
        brack_tab = ['[]','()','{}']
    if what_to_do == 'fix':
        brack_tab = ['()']
        left_added = 0
        right_added = 0
    
    while True:

        len1 = len(brackets2)
        for brack in brack_tab:
            brackets2 = brackets2.replace(brack,'')
        
        len2 = len(brackets2)
        if len1 == len2:
            if what_to_do == 'check':
                return 'Nie jest'
            if what_to_do == 'fix':
                brackets2 = '('+brackets2
                left_added += 1
            else:
                brackets2 = brackets2[1:]
                brackets2 = brackets2 +')'
                right_added += 1
        print(len2)
        if len2 == 0:
            if what_to_do == 'check':
                return 'Jest'
            
            if what_to_do == 'fix':
                return (left_added, right_added)
                break
brackets('fix', ')()(')