'''
1.  import module_name

2.  import module_name as alias_name

3.  from module_name import function_name

4.  from module_name import function_name as alias_name

5.  from module_name import *
'''

# Case 1
import random

for i in range(100):
    print(random.randint(1, 100)) # print a random integer between 1 and 100

# Case 2
import random as rd

for i in range(100):
    print(rd.randint(1, 100)) # print a random integer between 1 and 100

# Case 3
from random import randint

for i in range(100):
    print(randint(1, 100)) # print a random integer between 1 and 100

# Case 4
from random import randint as rdint

for i in range(100):
    print(rdint(1, 100)) # print a random integer between 1 and 100

# Case 5
from random import *

for i in range(100):
    print(randint(1, 100)) # print a random integer between 1 and 100
