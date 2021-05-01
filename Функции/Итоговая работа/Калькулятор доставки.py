def get_shipping_cost(quantity):
    if n == 1:
        return 1000
    elif n>1:
        return 1000+(120*(n-1))
n = int(input())
print(get_shipping_cost(n))