from itertools import permutations
import time

t1= time.time()
chaine = "HOMAWOOJohn"
c= 0
for i in permutations(chaine):
    print("".join(i))
    c+=1
t2 = time.time()
temps = t2 - t1
print(temps)
print(c)
#temps =4236.318062543869 ==70.60530104239781min
#c= 39.916.800
