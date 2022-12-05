import cProfile


# Ф-ція переведення в масив і розворота
def arrNumber(number):
    return [int(i) for i in list(number)]  # Додаємо елементи в масив з нашого "ліста" розвертаючи


# Ф-ція переведення в строку і розворота
def strNumber(number):
    if number == 0:
        return '0'
    return ''.join(str(i) for i in number)  # Формуємо строку розвертаючи


########################################################################################################################


# √ Ф-ція для вирівнювання по довжинні наших елементів
def sameLength(first, second):
    if len(first) > len(second):
        for i in range(len(first) - len(second)):  # Знаходимо різницю в кількості(дельту)
            second.insert(0, 0)  # Вирівнюємо другий додаючи в кінець(на перед, бо розвертали)
    if len(first) < len(second):
        for i in range(len(second) - len(first)):
            first.insert(0, 0)

    # print('first = ', first)
    # print('second = ', second)
    return first, second


def cyclicLeft(number, m):
    for i in range(m):
        number.append(number[0])
        number.pop(0)

    # print('number = ', number)
    return number


def cyclicRight(number, m):
    for i in range(m):
        number.insert(0, number[-1])
        number.pop(-1)
    return number


########################################################################################################################


def add(first, second):
    if first == 0:
        return second

    elif second == 0:
        return first

    if len(first) != len(second):
        first, second = sameLength(first, second)

    result = []
    for i in range(len(first)):
        result.append((first[i] + second[i]) % 2)

    # print('result = ', result)
    return result


def square(variable):
    result = cyclicRight(variable, 1)

    # print('result = ', result)
    return result


def trace(variable):
    result = 0
    for i in range(len(variable)):
        result = result + variable[i]

    result = result % 2
    # print('result = ', result)
    return result


def matrix(variable):
    result = []
    p = 2*variable + 1
    for i in range(variable):
        result.append([])
        for j in range(variable):
            i2, j2 = 2**i, 2**j
            if (i2+j2) % p == 1 or (i2-j2) % p == 1 or (-i2+j2) % p == 1 or (-i2-j2) % p == 1:
                result[i].append(1)
            else:
                result[i].append(0)

    # print('result = ', result)
    return result


def multMatrix(u, v):
    if type(v[0]).__name__ == 'list':
        v1 = len(v)
    else:
        v1 = 1

    u1 = len(u)
    result = []
    for i in range(v1):
        sum = 0
        for j in range(u1):
            if v1 == 1:
                sum = sum + u[j]*v[j]
            else:
                sum = sum + u[j]*v[i][j]
        result.append(sum % 2)

    # print('result = ', result)
    return result


def mult(u, v):
    landa = matrix(163)
    z = []
    for i in range(163):
        ui = cyclicLeft(u.copy(), i)
        vi = cyclicLeft(v.copy(), i)
        ulanda = multMatrix(ui, landa)
        ulandav = multMatrix(ulanda, vi)
        z.append(ulandav[0])

    # print('z = ', z)
    return z


def inverse(variable):
    t = arrNumber('10100010')
    result = variable.copy()
    k = 1
    for i in range(1, 8):
        result1 = result.copy()
        result = cyclicRight(result, k)
        result = mult(result, result1)
        k = k*2
        if t[i] == 1:
            result = mult(variable, square(result))
            k = k + 1

    result = square(result)

    # print('result = ', result)
    return result


def power(variable, extent):
    result = [1]*len(variable)
    m = len(extent)
    for i in range(m-1, -1, -1):
        if extent[i] == 1:
            result = mult(result, variable)
        variable = square(variable)

    # print('result = ', result)
    return result


first = '1111100010101010110101010101101010001111010101101011010101010111010101001110101010101101000111111101101010101011010101011011010011101011100010110101010010101010101'
second = '1101010101010101010101010111100001010101010101010010111100011110101010101010101011001010101010010101010100011101010100011110011010101100010101010101100101011010101'
third = '1111110000001010101001011101001101101011011101101101011010011010101010101010101011101111110101111010010010100101110110100101101100101011010101110011001010110111110'
extent = '1010001011111111111'

first = arrNumber(first)
second = arrNumber(second)
third = arrNumber(third)
extent = arrNumber(extent)


################################################################

# A)

res = strNumber(add(first, second))
print('\nfirst + second = ', res)

res = strNumber(mult(first, second))
print('\nfirst * second = ', res)

res = strNumber(square(first))
print('\nfirst^2 = ', res)

res = strNumber(power(first, extent))
print('\nfirst^extent = ', res)

res = strNumber(inverse(first))
print('\nfirst^-1 = ', res)

res = strNumber(trace(first))
print('\ntrace(first) = ', res)

################################################################

# Б)

# print('Пункт Б):\n')
# res1 = strNumber(mult(add(first, second), third))
# print('(a+b)*с = ', res1)
# res2 = strNumber(add(mult(first, third), mult(second, third)))
# print('(a*с + c*b) = ', res2)
# if res1 == res2:
#     print('\nПункт Б_1) - √\n')
# else:
#     print('Пункт Б_1) - десь помилка')

################################################################

# B)

# print('\nДодавання:')
# cProfile.run('add(first, second)')
# print('\nМноження:')
# cProfile.run('mult(first, second)')
# print('\nСлід:')
# cProfile.run('trace(first)')
# print('\nПіднесення до квадрату:')
# cProfile.run('square(first)')
# print('\nПіднесення до степення:')
# cProfile.run('power(first, extent)')
# print('\nЗнаходження оберненого:')
# cProfile.run('inverse(first)')
# print('\n')