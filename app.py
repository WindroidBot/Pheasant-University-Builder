from itertools import accumulate
import random
from nameDict import nationList, areaList, placeList, professList, scale
i = 0
while i < 20:
    a = random.sample(areaList, 1)
    b = random.sample(professList, 1)
    c = random.sample(scale, 1)
    print(a[0]+b[0]+c[0])
    i = i+1
