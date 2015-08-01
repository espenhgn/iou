#!/usr/bin/env python
'''I-owe-you calculation script after hiking trip into the bohemian paradise'''

people = ['EH', 'HB', 'JJ', 'PW']
CZK2EUR = 0.037


expenses = dict(
    car = dict(
        who =       ['EH'],
        amount =    [-3500,],
        currency =  ['CZK']),
    gas = dict(
        who =       ['EH'],
        amount =    [-1000,],
        currency =  ['CZK']),        
    hotel=dict(
        who  =      ['EH',  'PW'],
        amount =    [-3600, -3600],
        currency =  ['CZK', 'CZK']
    ),
    restaurant=dict(
        who  =      ['EH',],
        amount =    [-2000,],
        currency =  ['CZK',]        
    )
)

bank = dict(
    who =           ['HB',  'EH'],
    to  =           ['EH',  'JJ'],
    amount =        [1000,  400],
    what =          ['cash', 'food'],
    currency =      ['CZK', 'CZK'],
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
