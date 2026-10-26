# Case 1
import my_fun

print(my_fun.PI)
print(my_fun.NAME)

my_fun.log_seperator_1()
my_fun.log_seperator_2()
my_fun.log_seperator_3()


# Case 2
from my_fun import log_seperator_1, log_seperator_2, log_seperator_3, PI, NAME

log_seperator_1()
log_seperator_2()
log_seperator_3()

print(PI)
print(NAME)


# Case 3
from my_fun import *

log_seperator_1()
log_seperator_2()
log_seperator_3()

print(PI)
print(NAME)

