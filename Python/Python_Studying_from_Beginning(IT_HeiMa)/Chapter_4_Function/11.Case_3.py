"""
电商订单计算器
    定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。

具体规则如下：
    优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
    积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

def calculate_order_cost(*items, coupon=0, points=0, shipping=0):

    total = sum([item[1] * item[2] for item in items])

    # for item in items:
    #     name, price, quantity = item
    #     total += price * quantity

    if total >= 5000:
        total -= min(coupon, total)
        points_deduction = min((points // 100), total)
        total -= points_deduction

    total += shipping
    return total


products = [('item1', 1000, 3), ('item2', 2000, 2)]
print(calculate_order_cost(*products, coupon=500, points=300, shipping=50))