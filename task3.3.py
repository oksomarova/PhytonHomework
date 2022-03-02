# задание 3
def my_func(a,b,c):
    li = [a, b, c]
    m1 = max(li)
    li.remove(m1)
    m2 = max(li)
    res = m1 + m2
    return res
r = my_func(-5, 7, -3)
print('сумма двух наибольших чисел:', r)
