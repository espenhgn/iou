#!/usr/bin/env python
'''I-owe-you calculation script after hiking trip into the bohemian paradise'''
from __future__ import division

people = ['EH', 'HB', 'JJ', 'PW']
CZK2EUR = 1 / 27.14


expenses = dict(
    car = dict(
        who =       ['EH'],
        amount =    [-4247,],
        currency =  ['CZK']),
    gas = dict(
        who =       ['EH'],
        amount =    [-669,],
        currency =  ['CZK']),        
    hotel=dict(
        who  =      ['EH',  'PW'],
        amount =    [-3690, -3690],
        currency =  ['CZK', 'CZK']
    ),
    restaurant=dict(
        who  =      ['EH',],
        amount =    [-1951,],
        currency =  ['CZK',]        
    )
)

bank = dict(
    who =           ['HB',  'EH', 'JJ'],
    to  =           ['EH',  'JJ', 'PW'],
    amount =        [1000,  400, 5000],
    what =          ['cash', 'food', 'cash'],
    currency =      ['CZK', 'CZK', 'CZK'],
)


all_expenses = 0.
balance = dict(
    EH = 0.,
    HB = 0.,
    JJ = 0.,
    PW = 0.,
)

for k, v in expenses.items():
    for who, amount, currency in zip(v['who'], v['amount'], v['currency']):
        if currency == 'CZK':
            all_expenses += amount*CZK2EUR
            balance[who] += amount*CZK2EUR
        else:
            all_expenses += amount
            balance[who] += amount

for who, amount, currency, to in zip(bank['who'], bank['amount'],
                                     bank['currency'], bank['to']):
    if currency == 'CZK':
        balance[to] += amount*CZK2EUR            
        balance[who] -= amount*CZK2EUR
    else:
        balance[to] += amount            
        balance[who] -= amount

for who in people:
    balance[who] -= all_expenses/4



print('expenses in total:\tEUR %.2f' % all_expenses)
print('total per person:\tEUR %.2f' % (all_expenses/4.))

for k, v in balance.items():
    if v > 0:
        print('%s owes:\tEUR %.2f' % (k, v))
    else:
        print('%s receives:\tEUR %.2f' % (k, abs(v)))
