#program to demonstrate function
#task is to double each number in a list through function
import random

def double_list(list1):
    val = 0
    while val < len(list1):
        list1[val] = list1[val] * 2
        val += 1

list1 = []
for i in range(10):
    list1.append(random.randint(1,100))
    
print(list1)

double_list(list1)

print(list1)

    
