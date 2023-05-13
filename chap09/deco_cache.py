import random
from functools import lru_cache


@lru_cache
def get_0to100():
    return random.randint(0, 100)


print(get_0to100())
print(get_0to100())
