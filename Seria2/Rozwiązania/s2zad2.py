

tab = [1,2,3,4,3,2,3,1,0]


while True:
    swapped = False
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            tab[i], tab[i+1] = tab[i+1], tab[i]
            swapped = True
            
    if swapped == False:
        break
        
    
#%%

def bubble_sort(lst):
    n = len(lst)
    result = lst[:]

    while True:
        swapped = False
        
        for i in range(n - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        
        if not swapped:
            break

    return result

# wczytanie danych ze standardowego wejścia
numbers = list(map(int, input().split()))

# sortowanie
sorted_numbers = bubble_sort(numbers)

# wypisanie wyniku
print(*sorted_numbers)