import cProfile
A = str(int('D4D2110984907B5625309D956521BAB4157B8B1ECE04043249A3D379AC112E5B9AF44E721E148D88A942744CF56A06B92D28A0DB950FE4CED2B41A0BD38BCE7D0BE1055CF5DE38F2A588C2C9A79A75011058C320A7B661C6CE1C36C7D870758307E5D2CF07D9B6E8D529779B6B2910DD17B6766A7EFEE215A98CAC300F2827DB', 16))
B = str(int('3A7EF2554E8940FA9B93B2A5E822CC7BB262F4A14159E4318CAE3ABF5AEB1022EC6D01DEFAB48B528868679D649B445A753684C13F6C3ADBAB059D635A2882090FC166EA9F0AAACD16A062149E4A0952F7FAAB14A0E9D3CB0BE9200DBD3B0342496421826919148E617AF1DB66978B1FCD28F8408506B79979CCBCC7F7E5FDE7', 16))
C = str(int('269D7722EA018F2AC35C5A3517AA06EAA1949059AE8240428BBFD0A8BE6E2EBF91223991F80D7413D6B2EB213E7122710EDEC617460FA0191F3901604619972018EBEF22D81AED9C56424014CADCC2CCDEE67D36A54BFC500230CA6693ABA057B374746622341ED6D52FE5A79E6860F54F197791B3FEF49FD534CB2C675B6BDB', 16))

F = str(int('3A7EF2554E8940FA', 16))
M = str(int('69', 16))

# A = '91'
# B = '92'


# √ Ф-ція для переводу в двійкову систему
def smallConstantToLarge(number):
    string = ''
    number = int(number)
    while number > 0:
        string = str(number % 2) + string
        number = number // 2

    # print('number = ' + string + '\n')
    return string


# √ Ф-ція для порівняння
def longCmp(first, second):
    if len(first) > len(second):
        return 1
    elif len(first) < len(second):
        return -1
    else:
        for i in range(len(first)):
            if first[i] > second[i]:
                return 1
            if first[i] < second[i]:
                return -1
        return 0

# √ Ф-ція для додавання нулів на початку
def leftZeroAdd(number, amount):
    number = '0' * amount + number
    return number


# √ Ф-ція для зсуву цифр у бік старших індексів
def longShiftDigitsToHigh(temp, i):
    for k in range(i):
        temp = temp + '0'
    # print('temp = ' + temp)
    return temp


# √ Ф-ція для додавання, повертає в двійковому
def longAdd(first, second):
    firstStr = str(first)
    secondStr = str(second)
    Result = ''
    if len(firstStr) > len(secondStr):
        delta = len(firstStr) - len(secondStr)  # Різниця в кількості цифр
        secondStr = leftZeroAdd(secondStr, delta)  # Створюю додаткові нулі на початку
        # print(secondStr)
    if len(firstStr) < len(secondStr):
        delta = len(secondStr) - len(firstStr)  # Різниця в кількості цифр
        firstStr = leftZeroAdd(firstStr, delta)  # Створюю додаткові нулі на початку
        # print(firstStr)
    firstStr = firstStr[::-1]  # Розвертаю для зручнішого для себе способу
    secondStr = secondStr[::-1]
    # print(firstStr)
    # print(secondStr)
    carry = 0

    for i in range(len(firstStr)):  # додаю по розрядах
        dischargeFirst = int(firstStr[i])
        dischargeSecond = int(secondStr[i])
        temp = dischargeFirst + dischargeSecond + carry
        Result = str(temp % 2) + Result
        carry = temp // 2
    # print("A + B = " + hex(int((str(carry) + Result), 2)) + '\n')
    return str(carry) + Result


# √ Ф-ція для віднімання, повертає в двійковому
def longSub(first, second):
    firstStr = str(first)
    secondStr = str(second)
    Result = ''
    cmp = longCmp(firstStr, secondStr)
    if cmp == 1 or cmp == 0:
        if len(firstStr) > len(secondStr):
            delta = len(firstStr) - len(secondStr)
            secondStr = leftZeroAdd(secondStr, delta)  # Створюю додаткові нулі на початку
            # print(secondStr)
        firstStr = firstStr[::-1]
        secondStr = secondStr[::-1]
        # print('firstStr = ' + firstStr)
        # print('secondStr = ' + secondStr)
        borrow = 0
        for i in range(len(firstStr)):  # віднамання по розрядах
            dischargeFirst = int(firstStr[i])
            dischargeSecond = int(secondStr[i])
            temp = dischargeFirst - dischargeSecond - borrow
            if temp >= 0:
                Result = str(temp) + Result
                borrow = 0
            elif temp < 0:
                Result = str(2 + temp) + Result
                borrow = 1
        # print('різицяДо = ' + Result)
        while Result[0] != '1' and len(Result) > 1:  # Відрізаю зайві нулі на початку
            Result = Result[1:]
        # print("A - B = " + hex(int(Result, 2)))
        # print('різиця = ' + Result)
        return Result
    else:
        print('Ви віднімаєте від меншого більше, введіть коректні данні')


# √ Ф-ція для множення на цифру, повертає в двійковому
def longMulOneDigit (first, digit):
    first = str(first)
    Result = ''
    carry = 0
    digit = int(digit)
    # print(digit)
    for i in range(len(first) - 1, -1, -1):
        dischargeFirst = int(first[i])
        temp = dischargeFirst * digit + carry
        Result = str(temp % 2) + Result
        carry = temp // 2
    if carry == 0:
        # print("A * b = " + hex(int(Result, 2)))
        return Result
    else:
        Result = str(carry) + Result
        # print("A * b = " + hex(int(Result, 2)))
        return Result


# √ Ф-ція для множення багаторозрядних, повертає в двійковому
def longMul(first, second):
    firstStr = str(first)
    secondStr = str(second)
    Result = ''
    if len(firstStr) > len(secondStr):
        delta = len(firstStr) - len(secondStr)
        secondStr = leftZeroAdd(secondStr, delta)  # Створюю додаткові нулі на початку
        # print('secondStr = ' + secondStr)
    if len(firstStr) < len(secondStr):
        delta = len(secondStr) - len(firstStr)
        firstStr = leftZeroAdd(firstStr, delta)  # Створюю додаткові нулі на початку
    for i in range(len(firstStr) - 1, -1, -1):
        temp = longMulOneDigit(first, secondStr[i])
        amountZero = abs(i - len(firstStr) + 1)
        temp = longShiftDigitsToHigh(temp, amountZero)
        if i == len(firstStr) - 1:
            Result = temp
        else:
            if len(Result) < len(temp):
                Result = '0' + Result
            Result = longAdd(Result, temp)
        while Result[0] != '1' and len(Result) > 1:  # Відрізаю зайві нулі на початку
            Result = Result[1:]
    # print("\nA * B = " + hex(int(Result, 2)))
    # print('Result = ' + Result)
    return Result


# √ Ф-ція для піднесення чисел до багаторозрядного степеня, повертає в двійковому
def longPower1(first, extent):
    Result = '1'
    firstStr = str(first)
    extent = list(extent)  # В масив нащустепіль двійкову
    extent.reverse()  # Розвертаю як в алгоритмі
    for i in extent:
        if i == '1':
            Result = longMul(Result, firstStr)
        firstStr = longMul(firstStr, firstStr)

    # print('Res = ' + hex(int(Result, 2)))
    return Result


# √ Ф-ція для оформлення остачі
def particle(Q, delta):
    if len(Q) > delta:
        Q = list(Q)  # В масив її перетворюю
        Q.reverse()  # Розвертаю
        Q[delta] = '1'  # Ставдю в кінець частку
        Q.reverse()  # Розвертаю і часка вже йде спочатку як треба
        # print(''.join(Q))
    else:
        Q = list(Q)  # В масив її
        Q.append('1')  # додаю в кінець
        Q = ''.join(Q)  # перетворюю в строку для використання у функції
        Q = longShiftDigitsToHigh(Q, delta)  # Зміщую
        # print(''.join(Q))
    return ''.join(Q)  # Повертаю все ж таки строку для інших махінацій


# √ Ф-ція ділення та знаходження остачі
def longDivMod(first, second):
    firstStr = str(first)
    secondStr = str(second)
    k = len(secondStr)
    # print('k = ' + str(k))
    # print('1 = ', firstStr)
    # print('2 = ', secondStr)
    R = firstStr
    Q = ''
    cmp = longCmp(firstStr, secondStr)
    if cmp == 1 or cmp == 0:  # Перевірка яке на яке дылимо
        while longCmp(R, secondStr) == 1 or longCmp(R, secondStr) == 0:
            t = len(R)
            # print('t = ' + str(t))
            C = longShiftDigitsToHigh(secondStr, t - k)
            # print('C = ' + C)

            if longCmp(R, C) == -1:
                t = t - 1
                C = longShiftDigitsToHigh(secondStr, t - k)
                # print('C = ' + C)

            R = longSub(R, C)
            # print('R = ' + R)
            Q = particle(Q, t-k)
            # print('Q = ' + str(Q))

    else:  # Якщо Ділене < Дільник
        Q = '0'
        R = firstStr
    # print('R = ' + hex(int(R, 2)))
    # print('Q = ' + hex(int(Q, 2)))
    return Q, R


######################################################################################


A = smallConstantToLarge(A)
# print('A = ', A)
B = smallConstantToLarge(B)
# print('B = ', B)
C = smallConstantToLarge(C)
# print('C = ', C)
F = smallConstantToLarge(F)
M = smallConstantToLarge(M)
N = str(int('101'))
N = smallConstantToLarge(N)

# A)
# print(" ")
# K = longAdd(A, B)
# print('A + B = ', hex(int(K, 2)))

# K = longSub(A, B)
# print('A - B = ', hex(int(K, 2)))

# longMulOneDigit(A, B)

# K = longMul(A, B)
# print('A * B = ', hex(int(K, 2)))

# longMul(A, A)

# K = longDivMod(longMul(A, B), B)[0]
# D = longDivMod(longMul(A, B), B)[1]
# print('Q = ', hex(int(K, 2)))
# print('R = ', hex(int(D, 2)))

# K = longPower1(F, M)
# print('A ^ B = ', hex(int(K, 2)))

######################################################################################

# Б)
# print('Пункт Б_1):')
# res1 = longMul(longAdd(A, B), C)
# print('(a + b)*c = ', hex(int(res1, 2)))
# res2 = longMul(C, longAdd(A, B))
# print('c*(a + b) = ', hex(int(res2, 2)))
# res3 = longAdd(longMul(A, C), longMul(B, C))
# print('a*c + b*c = ', hex(int(res3, 2)))
#
# if res1 == res2 and res2 == res3:
#     print('Пункт Б_1) - √\n')
# else:
#     print('Пункт Б_1) - десь помилка')

# print('Пункт Б_2):')
# res4 = longMul(N, A)
# print('n*a = ', hex(int(res4, 2)))
# res5 = '0'
# for i in range(101):
#     res5 = longAdd(res5, A)
# print('a+...+a = ', hex(int(res5, 2)))
#
# while res5[0] != '1' and len(res5) > 1:  # Відрізаю зайві нулі на початку
#     res5 = res5[1:]
#
# if res4 == res5:
#     print('Пункт Б_2) - √')

######################################################################################

# В)
# print('\nПункт В):\n')
# print('\nДодавання')
# cProfile.run('longAdd(A, B)')
# print('\nВіднімання')
# cProfile.run('longSub(A, B)')
# print('\nМноження')
# cProfile.run('longMul(A, B)')
# print('\nДілення')
# cProfile.run('longDivMod(longMul(A, B), B)')
# print('\nПіднесення до ступеня')
# cProfile.run('longPower1(F, M)')

