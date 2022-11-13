import cProfile


# Ф-ція переведення в масив і розворота
def arrNumber(number):
    return [int(i) for i in list(number)[::-1]]  # Додаємо елементи в масив з нашого "ліста" розвертаючи


# Ф-ція переведення в строку і розворота
def strNumber(number):
    if number == 0:
        return '0'
    return ''.join(str(i) for i in number[::-1])  # Формуємо строку розвертаючи


########################################################################################################################

# √ Ф-ція для вирівнювання по довжинні наших елементів
def sameLength(first, second):
    if len(first) > len(second):
        for i in range(len(first) - len(second)):  # Знаходимо різницю в кількості(дельту)
            second.append(0)  # Вирівнюємо другий додаючи в кінець(на перед, бо розвертали)
    if len(first) < len(second):
        for i in range(len(second) - len(first)):
            first.append(0)

    # print('first = ', first)
    # print('second = ', second)
    return first, second


# √ Ф-ція для видалення нулів з кінця
def removeZero(number):
    if number == 0:
        return number

    if len(number) == 1 and number[0] == 0:
        return 0

    while number[-1] == 0:
        if len(number) == 1 and number[0] == 0:
            return 0
        number.pop(-1)

    # print('number = ', number)
    return number


# √ Ф-ція для здвигу до вищіх розрядів
def shiftToHigh(array, k):
    result = array.copy()  # Копіюємо масив
    for i in range(k):
        result.insert(0, 0)  # Вставляємо 0 на перед(тобто назад бо розвертали)

    # print('result', result)
    return result


# √ Ф-ція для здвигу вправо
def shiftRight(number, k):
    for i in range(k):
        number.insert(0, 0)  # Вставляємо 0 на перед
        number.pop(-1)

    # print('number = ', number)
    return number


# √ Ф- ція для порівняння
def cmp(first, second):
    # Зрізаємо зайві нулі спереді(тобто зкінця, бо розвертали)
    first = removeZero(first)
    second = removeZero(second)

    if first != 0:
        lenFirst = len(first)
    else:
        lenFirst = 0

    if second != 0:
        lenSecond = len(second)
    else:
        lenSecond = 0

    if lenFirst > lenSecond:
        # print('first is bigger')
        return 1
    elif lenFirst < lenSecond:
        # print('second is bigger')
        return -1
    else:
        for i in range(len(first) - 1, -1, -1):
            if first[i] == second[i]:
                pass
            elif first[i] > second[i]:
                # print('first is bigger')
                return 1
            else:
                # print('second is bigger')
                return -1

    # print('same')
    return 0

########################################################################################################################


# √ Ф-ція для модуля
def modulePolynom(number):
    ourMod = [0] * 164  # 164, бо 164 доданки від х^0 до x^163
    ourMod[163], ourMod[7], ourMod[6], ourMod[3], ourMod[0] = 1, 1, 1, 1, 1

    result = divPolynom(number, ourMod)[1]
    # print('result = ', result)
    return result


# √ Ф-ція для відніманян поліномів
def subPolynom(first, second):

    if first == 0:
        return second
    elif second == 0:
        return first

    if len(first) != len(second):
        first, second = sameLength(first, second)

    result = []
    for i in range(len(first)):
        result.append((first[i] - second[i]) % 2)  # Віднімаємо по розрядно

    result = modulePolynom(result)
    # print('result = ', result)
    return result


# √ Ф-ція для ділення поліномів
def divPolynom(first, second):
    first = removeZero(first)
    compare = cmp(first, second)
    if compare == 0:
        return 0
    if compare == -1:
        return 0, first

    k = len(second)
    r = first.copy()
    q = [0] * len(first)

    while cmp(r, second) != -1:
        t = len(r)
        c = shiftToHigh(second, t - k)  # Зсуваємо до вищіх розряів
        r = subPolynom(r, c)  # Віднімаємо від "остачі" отримане, поки не отримаємо остачу мену за дільник
        q[t - k] = 1

    q = removeZero(q)
    r = removeZero(r)
    # print('q = ', q)
    # print('r = ', r)
    return q, r


# √ Ф-ція для додавання поліномів
def addPolynom(first, second):
    if first == 0:
        return second
    elif second == 0:
        return first

    if len(first) != len(second):
        first, second = sameLength(first, second)

    result = []
    for i in range(len(first)):
        result.append((first[i] + second[i]) % 2)  # Порозрядне додавання

    result = modulePolynom(result)  # Знаходимо по модулю
    # print('result = ', result)
    return result


# √ Ф-ція для множення поліномів
def multPolynom(first, second):
    if first == 0 or second == 0:
        return 0

    if len(first) != len(second):
        first, second = sameLength(first, second)

    result = [0] * 2 * len(first)
    for i in range(len(first)):
        if first[i] == 0:
            continue
        for j in range(len(second)):
            if second[j] == 0:
                continue
            result[i+j] = (result[i+j] + first[i] * second[j]) % 2

    result = modulePolynom(result)
    # print('result = ', result)
    return result


# √ Ф-ція для конвертування
def trace(variable):
    result = variable
    for i in range(0, 163 - 1):
        variable = modulePolynom(squarePolynom(variable))
        result = modulePolynom(addPolynom(result, variable))

    # print('result = ', result)
    return result


# √ Ф-ція для піднесення до квадрату
def squarePolynom(variable):
    result = multPolynom(variable, variable)

    # print('result = ', result)
    return result


# √ Ф-ція для піднесення до ступення за горнером
def powerPolynom(variable, extent):
    k = len(extent)
    result = [0] * k
    result[0] = 1
    for i in range(k - 1, -1, -1):

        if extent[i] == 1:
            result = multPolynom(result, variable)
            result = modulePolynom(result)
        if i != 0:
            result = multPolynom(result, result)
            result = modulePolynom(result)

    # print('result = ', result)
    return result


# √ Ф-ція для знаходженян оберненого елемента
def inverse(variable):
    result = variable
    for i in range(0, 163 - 2):
        variable = modulePolynom(squarePolynom(variable))  # Підносимо в кварат
        result = modulePolynom(multPolynom(result, variable))  # Мнодимо на result i variable

    result = modulePolynom(squarePolynom(result))
    # print('result = ', result)
    return result


##################################

first = '1111100010101010110101010101101010001111010101101011010101010111010101001110101010101101000111111101101010101011010101011011010011101011100010110101010010101010101'
second = '1101010101010101010101010111100001010101010101010010111100011110101010101010101011001010101010010101010100011101010100011110011010101100010101010101100101011010101'
extent = '1101010101110111011010101010100011010101010000110100101000010101101111110101110110011101001011010010100101010101010101010101101001010010010101001000011110110110111'

first = arrNumber(first)
second = arrNumber(second)
extent = arrNumber(extent)

################################################################

# A)

# res = strNumber(addPolynom(first, second))
# print('\nfirst + second = ', res)
#
# res = strNumber(multPolynom(first, second))
# print('\nfirst * second = ', res)
#
# res = strNumber(squarePolynom(first))
# print('\nfirst^2 = ', res)
#
# res = strNumber(powerPolynom(first, extent))
# print('\nfirst^extent = ', res)
#
# res = strNumber(inverse(first))
# print('\nfirst^-1 = ', res)
#
# res = strNumber(trace(first))
# print('\ntrace(first) = ', res)
#
# res = strNumber(trace(second))
# print('\ntrace(second) = ', res)
#
# res = strNumber(trace(extent))
# print('\ntrace(extent) = ', res)

################################################################

# Б)

# print('Пункт Б):\n')
# res1 = strNumber(multPolynom(addPolynom(first, second), extent))
# print('(a+b)*с = ', res1)
# res2 = strNumber(addPolynom(multPolynom(first, extent), multPolynom(second, extent)))
# print('(a*с + c*b) = ', res2)
# if res1 == res2:
#     print('\nПункт Б_1) - √\n')
# else:
#     print('Пункт Б_1) - десь помилка')

################################################################

# B)

# print('\nДодавання:')
# cProfile.run('addPolynom(first, second)')
# print('\nМноження:')
# cProfile.run('multPolynom(first, second)')
# print('\nСлід:')
# cProfile.run('trace(first)')
# print('\nПіднесення до квадрату:')
# cProfile.run('squarePolynom(first)')
# print('\nПіднесення до степення:')
# cProfile.run('powerPolynom(first, extent)')
# print('\nЗнаходження оберненого:')
# cProfile.run('inverse(first)')
# print('\n')
