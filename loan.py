#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
# Licence:     Apache License Version 2.0
# ---------------------------------------------
# M = L(I(1 + I)**N) / ((1 + I)**N - 1)
# M = Monthly Payment, L = Loan, I = Interest, N = Number of payments,
# Interés = Monto_Solicitado * ((1 + 25%) ^ (Plazo / 360) - 1)
# cifras en miles


WIDTH = 10
PRECISION = 3


def interest(capital, plazo=30, tasa=0.25):
    return round(capital * ((1 + tasa) ** (plazo / 360) - 1), 3)


def get_cuota(capital, plazo, tasa):
    return round((capital * tasa) / (1 - ((1 + tasa) ** -plazo)), 0)


def plan_de_pagos(capital, plazo, tasa):
    cuota = get_cuota(capital, plazo, tasa)
    mes, interes, amortizacion, data = 0, 0, 0, dict()
    print('{:^10}{:^10}{:^10}{:^10}{:^10}'.format(
        'mes', 'couta', 'interes', 'amortizacion', 'saldo'))
    data['plan'] = list()
    while mes <= plazo:
        data['plan'].append(
            dict(
                mes=mes,
                cuota=cuota,
                interes=interes,
                amortizacion=amortizacion,
                saldo=capital,
            )
        )
        # print('{:^10}{:^10}{:^10}{:^10}{:^10}'.format(
        #     mes, cuota, interes, amortizacion, capital))
        interes = round(capital * tasa, 0)
        amortizacion = round(cuota - interes, 0)
        capital -= amortizacion
        mes += 1
    return data
