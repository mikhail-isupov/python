from sympy import *
#Поиск координат x для которых выполняется f(x)=g(x) === поиск корней уравнения f(x)-g(x)=0
x = Symbol('x')
f = x**3 - 50*x
g = -x**4 + 88*x**2 - 241

for root in real_roots(f-g):
    x_num = root.evalf()
    f_num = f.subs(x, x_num)
    g_num = g.subs(x, x_num)
    print(f'x={round(x_num,2)} f(x)={round(f_num,2)} g(x)={round(g_num,2)}')

