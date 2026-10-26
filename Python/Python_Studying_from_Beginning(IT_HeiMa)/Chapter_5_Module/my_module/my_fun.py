# Constants and Functions

PI = 3.1415926  # Constant

NAME = 'C_J_N-' # Constant

def log_seperator_1():
    print('-' * 30)

def log_seperator_2():
    print('+' * 30)

def log_seperator_3():
    print('#' * 30)

def log_seperator_4():
    print('*' * 30)

'''
__name__  
    # Special built-in variable that represents the name of the module
    # If the module is run directly, __name__ will be '__main__'
    # If the module is imported, __name__ will be the module's name
    # It is commonly used to check if the module is being run directly or imported

__main__
    # Special built-in variable that represents the name of the top-level script environment
    # When a module is run directly, __main__ will be '__main__'
    # When a module is imported, __main__ will not be '__main__'
    # It is commonly used to check if the script is the main program being executed
'''

print(__name__)

# Check if the module is being run directly or imported
if __name__ == '__main__':
    print('This module is being run directly.')
    log_seperator_1()


'''
__all__
    # List of public objects of this module
    # When using 'from my_fun import *', only these will be imported
   
    Example:
    __all__ = ['PI', 'NAME', 'log_seperator_1', 'log_seperator_2', 'log_seperator_3', 'log_seperator_4']
'''
__all__ = ['PI', 'NAME', 'log_seperator_1', 'log_seperator_2', 'log_seperator_3', 'log_seperator_4']    