#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input("Введите список из 10 элементов: ").split()))
    summ = 0
    k = 0  # количество условий удовлетворяющих условию
    # Проверить количество элементов списка
    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    for i in a:
        if (2 < i < 20) and (i % 8 == 0):
            k = k + 1
            summ = summ + i

    if summ != 0:
        print("Количество элементов удовлетворяющих условию: ", k)
        print("Сумма элементов: ", summ)
    else:
        print("В списке нет элементов удовлетворяющих условию.")
