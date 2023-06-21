#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = int(input("Покупатель должен заплатить в кассу: "))
    k1, k2, k5, k10, k100, k500 = 0, 0, 0, 0, 0, 0
    while s != 0:
        if s >= 500:
            s -= 500
            k500 += 1
        if (s >= 100) and (s < 500):
            s -= 100
            k100 += 1
        if 10 <= s < 100:
            s -= 10
            k10 += 1
        if 5 <= s < 10:
            s -= 5
            k5 += 1
        if 2 <= s < 5:
            s -= 2
            k2 += 2
        if 1 <= s < 2:
            s -= 1
            k1 += 1

    print("1 руб.: ", k1)
    print("2 руб.: ", k2)
    print("5 руб.: ", k5)
    print("10 руб.: ", k10)
    print("100 руб.: ", k100)
    print("500 руб.: ", k500)
