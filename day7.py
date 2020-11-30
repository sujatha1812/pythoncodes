#sys package to find python path
import sys
sys.path

#random function

import random
for x in range(5):
    print(random.randint(1,101))

#pandas package

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"]}
import pandas as pd
bb = pd.DataFrame(dict)
print(bb)

#create a module to link to another py file#
def sum(a,b):
    return a+b
myList=[1,2,3,4,5]


import Addition
print (Addition.sum(2,3))
Addition.myList


