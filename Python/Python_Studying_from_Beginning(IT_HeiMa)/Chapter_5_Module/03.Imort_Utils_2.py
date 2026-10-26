# Using from my_utils import * to access all utilities directly
# Add __all__ = [] in my_utils/__init__.py to control what gets imported with *

from my_utils import *

my_fun.log_seperator_1()

print(my_var.PI)
print(my_var.NAME)

my_fun.log_seperator_2()