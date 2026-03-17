

names = ['ala','ania','ala', 'basia', 'kasia', 'ania',
         'basia', 'ala']

names = [1,1,1,1,1,1,1,2,3,2,1,1,1,4]

count_list = []


b = list(set(names))
for i in range(len(b)):
    name_local_set = b[i]
    count = 0
    for name in names:
        
        if name == name_local_set:
            count += 1
    count_list.append(count)
    
result = [(key, value) for key, value in zip(b, count_list)
           if value == max(count_list)]

print(result)

#%%


def most_frequent(tab):
    
    tab_set = list(set(tab))
    count_list = []
    
    for i in range(len(tab_set)):
        el_local = tab_set[i]
        count = 0
        for el in tab:
            
            if el == el_local:
                count += 1
        count_list.append(count)
        
    result = [(key, value) for key, value 
              in zip(tab_set, count_list)
               if value == max(count_list)]

    return result

lst = list(input().split())

print(most_frequent(lst))