def div(a, b):
    return a / b

def smart_div(func):
    def inner(c, e):
        if c < e:
            c, e = e, c
        return func(c, e)
    return inner

div = smart_div(div)
print(div(3, 12))