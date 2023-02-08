import numpy as np
from numpy import random


cape_canaveral = np.array([["28", "0.4740"], ["-80", "0.5772"]])
print(f"Координаты мыса Канаверал: \n{cape_canaveral}\n")

while True:
    rand_lat = random.randint(-90, 90)
    rand_long = random.randint(-180, 180)
    flat = round(random.rand(), 4)
    flong = round(random.rand(), 4)
    lat = np.stack((str(rand_lat), str(flat)))
    long = np.stack((str(rand_long), str(flong)))
    coords = np.stack((lat, long))
    print(f"Случайные координаты: \n{coords}")
    input()