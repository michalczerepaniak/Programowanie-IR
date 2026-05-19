import numpy as np


#%% Zadanie 2

inflacja = (
    np.array([[9.4, 16.6, 3.7],
               [8.5, 18.4, 2.8],
               [11.0, 16.1, 2.0],
               [12.4, 14.7, 2.4],
               [13.9, 13.0, 2.5],
               [15.5, 11.5, 2.6],
               [15.6, 10.8, 4.2],
               [16.1, 10.1, 4.3],
               [17.2, 8.2, 4.9],
               [17.9, 6.6, 5.0],
               [17.5, 6.6, 4.7],
               [16.6, 6.2, 4.7]]))

#2.1
print(inflacja[3,1])

#2.2
print(inflacja[:,0])

#2.3
print(inflacja[4,:])

#2.4
print(inflacja[5:8,:])

#2.5
print(inflacja[3::4,:])

#2.6
print(np.mean(inflacja, axis = 0))

#2.7
print(np.mean(inflacja, axis = 1))

#2.8
print(inflacja.shape)

#2.9
print(inflacja.T)

#2.10
inflacja_kwart = inflacja.T.reshape((-1,4))
print(np.mean(inflacja_kwart, axis = 1))

#2.11
inflacja2 = np.copy(inflacja)
inflacja2[np.logical_or(inflacja2 > 10, inflacja2 <3)] = 0
print(inflacja2)

#%% Zadanie 3
import random

np.random.seed(4321)
oceny = np.round(3 * np.random.random_sample((100,)) + 2, 2)

oceny[oceny < 2.8] = 2
oceny[np.logical_and(oceny >= 2.8, oceny < 3.7)] = 3
oceny[np.logical_and(oceny >= 3.7, oceny < 4.5)] = 4
oceny[oceny >= 4.5] = 5
print(oceny)


#%% Zadanie 4
np.random.seed(4321)
wyniki_cw = np.random.randint(101, size=(100,10))

#4.1 jak wyzej

#4.2
srednia_test = np.mean(wyniki_cw, axis = 0)
print(np.where(srednia_test == np.max(srednia_test)))
#Czyli test nr 6

#4.3
srednia_osobowa = np.mean(wyniki_cw, axis = 1)
srednia_sort = np.sort(srednia_osobowa)
prog = srednia_sort[-7]
print(prog)


#%% Zadanie 4.5 i 5
#jak wyzej

#%% Zadanie 6

a = np.array([1,2,3,4])
b = np.array([4,3,2,1])

#6.1

dist = np.linalg.norm(a-b)
# lub ręcznie
dist2 = np.sqrt(np.sum((a-b)**2))

#6.2

print(a,b, a-b, dist)

#%%Zadanie 7

temperatury = [-1, 1, 6, 12, 17, 21, 24, 23, 18, 12, 6, 1]
temps = np.array(temperatury)

print(np.mean(temps),
      np.max(temps),
      np.mean(temps),
      np.std(temps))

print(np.where(temps == np.max(temps)))
print(np.where(temps == np.min(temps)))

print(temps - np.mean(temps))


