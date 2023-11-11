import random
import string


def generate_random_list(length,start,end):
    if start < end:
        return [random.randint(start,end) for _ in range(length)]
list = generate_random_list(random.randint(5,30),1,random.randint(2,1000))
print(list)



print(' '.join([1,2,3]))