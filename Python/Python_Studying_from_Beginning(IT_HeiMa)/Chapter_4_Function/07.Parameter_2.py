"""
不定长参数（可变参数）：参数个数不确定
"""

"""
不定长参数——位置传递
"""
def calc_data1(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    return min_data, max_data, round(avg_data, 3)

data1 = calc_data1(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(data1)


"""
不定长参数——关键字传递
"""
def calc_data2(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)


    if kwargs["round"]:
        avg_data = round(avg_data, kwargs["round"])

    if kwargs["print"]:
        print("print is True")
        
    return min_data, max_data, avg_data

data2 = calc_data2(10, 20, 30, 6, 50, round=3, print=True)
print(data2)