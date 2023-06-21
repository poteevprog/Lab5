#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = list(map(float, input("Введите список: ").split()))
    a = float(input("Введите A: "))
    b = float(input("Введите B: "))
    summ = 0
    k = 0  # Элементы лежащие в диапазоне от A до В
    maxi = s[0]  # Макс == значение первого элемента
    j = 1
    t = 0

    if len(s) == 0:
        print("Неверный размер списка!", file=sys.stderr)
        exit(1)

    for i in s:
        if a < i < b:
            k += 1

        t = t + 1

        if i > maxi:
            maxi = i
            j = t  # индекс макс значения

    # Сумма элементов после макс. значения
    for i in range(len(s)):
        if i > j - 1:
            summ += s[i]

    # Упорядочить элементы списка по возрастанию модуля
    s1 = s
    for i in range(len(s)):
        s1[i] = abs(s1[i])

    s1.sort()
    s = s1

    print("Упорядоченный список: ", s)
    print("Количество элементов списка лежащих в диапазоне от A до В: ", k)
    print("Сумма элементов списка, рассположенных после максимального элемента: ", summ)
