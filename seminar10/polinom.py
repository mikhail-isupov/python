#Модуль для работы с полиномами
def polinom_to_vector(data):
    DIGITS = '+.0123456789'
    polinom = []
    for s in data: #Преобразование строки
        if s == '-':
            polinom.append('+') #оператор минус превращается в унарный оператор
            polinom.append(s)
        elif s in DIGITS:
            polinom.append(s)
        elif s.isalpha():
            polinom.append('x') #Стандартное имя для аргумента
    
    polinom = ''.join(polinom) #Отфильтрован, остались только цифры, аргумент, знаки сложения и унарные операторы
    pol_terms = polinom.split('+') #Отдельные члены многочлена в виде списка
    decomposed_polinom = {} #тут будут храниться найденные степени полинома и его коэффициенты

    for term in pol_terms:
        if term:
            term_coeffs = term.split('x') #Разбиваем член многочлена на пару коэффициент:степень
            if len(term_coeffs) == 1:
                term_coeffs.append('0') #постоянный член полинома соответствует x^0
            if not term_coeffs[0]:
                term_coeffs[0] = '1' #Это если нам попался ...+xn+...
            elif term_coeffs[0] == '-':
                term_coeffs[0] = '-1' #Это если нам попался ...+-xn+....
            if not term_coeffs[1]:
                term_coeffs[1] = '1' #Это если попался ...+nx+...
            decomposed_polinom[term_coeffs[1]] = term_coeffs[0] #степень это ключ а коэффициент это значение
    max_power = int(max(decomposed_polinom)) #Максимальная степень полинома
    polinom_as_vector = [0] * (max_power + 1)
    for i in range(max_power + 1):
        key = str(i)
        if key in decomposed_polinom:
            polinom_as_vector[i] = float(decomposed_polinom[key])
    return polinom_as_vector

def vector_to_polinom(data):
    output_string=''
    for i in range(len(data) - 1, -1, -1):
        if data[i]:
            sum = '+' if data[i] > 0 and i < len(data) - 1 else '' #Ставить или не ставить знак плюс между членами
            if i==0:
                power = ''
            elif i==1:
                power ='x'
            else:
                power ='x^' + str(i) #Собираем аргументы
            coeff = data[i] if data[i] - int(data[i]) else int(data[i]) #Если коэффициент целый то преобразуем к int
            if coeff == 1 and i > 0:
                term_coeff = '' #Если коэффициент == 1 то его не пишем
            elif coeff == -1 and i > 0:
                term_coeff = '-' #А если -1 то знак минус нужен
            else:
                term_coeff = str(coeff)
            output_string += sum + term_coeff + power
    return output_string

def convert(data=None):
    #Преобразование полинома в вектор и обратно, либо возврат False если данные не в том формате или их нет
    if data and isinstance(data, str):
        return polinom_to_vector(data)
    elif data and isinstance(data, list):
        return vector_to_polinom(data)
    else:
        return False

#Модуль для работы с векторами
def sum(a, b): #сумма двух векторов
    max_len = max(len(a), len(b)) #Максимальная длина вектора
    result = [0] * max_len
    for i in range(max_len):
        result[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return result