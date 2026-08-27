"""
    import module_name as nm
    module_name 是模块的名称，nm 是给模块指定的别名
    使用别名后，可通过指定的别名来调用模块中的函数

    module_name.function_name()
    nm.function_name()
"""

import module_pizza as mp
mp.make_pizza(16, 'pepperoni')
mp.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


"""
    导入特定的函数
    from module_name import function_name
    from module_name import function_name as fn
    
    from module_name import function_0, function_1, function_2
    from module_name import *

"""