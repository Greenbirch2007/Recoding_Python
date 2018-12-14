# ７．３　使用装饰器改进"策略"模式

# 使用注册装饰器可以改进之前电商的折扣示例


# 前面示例的主要问题是，定义体中有函数的名称，但是best_promo用来判断哪个折扣幅度最大的promos列表欧中也有函数名称。这种重复是个问题
# 因为新增策略函数后可能会忘记把它添加到promo列表中，导致best_promo忽略新策略，而且不报错，为系统引入不易察觉的缺陷

# 示例７．３　　promos列表中的值使用promotion装饰器填充


promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    '''为积分为１０００或以上的顾客提供5%折扣'''
    return order.total() * .05 if order.customer.fidelity  >= 1000 else 0


@promotion
def bulk_item(order):
    '''单个商品为２０个以上时提供５％折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() *.1
    return discount

@promotion
def large_order(order):
    '''订单中的不同商品达到１０个或以上时提供７％折扣'''
    distinct_items=  {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total()  * .07
    return 0




def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)


# 注意到best_promos无需修改，因为它依赖promos列表


# 这个方案的优势
# １．促销策略函数无需使用特殊的名称(即不用以_promo结尾)
# ２．　@promotion装饰器突出了被装饰器的函数的作用，还便于禁用某个促销策略：只需要把装饰器注销掉即可
# 3. 促销折扣策略可以在其他模块中定义，在系统中的任何地方都行，只要使用＠promotion装饰器注释掉
#  4.促销折扣策略可以在其他模块中定义，在系统中的任何地方都行，只要使用@promotion装饰器即可

#不过，多数装饰器会修改被装饰的函数。通常，它们会定义一个内部函数，然后将其返回，替换被装饰的函数。使用内部函数的代码几乎都要靠闭包才能正确运作。
# 为了理解闭包，我们要最后一步，先了解python中的变量作用域

