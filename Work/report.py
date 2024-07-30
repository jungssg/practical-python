# report.py
#
# Exercise 2.4

import csv

#이전 코드
def portfolio_cost(filename):
    '''포트폴리오 파일의 총 비용(주식수*가격)을 계산''' 
    total_cost = 0.0
    with open(filename, 'rt') as f: 
        rows = csv.reader(f) 
        headers = next(rows)
    for row in rows:
        nshares = int(row[1])
        price = float(row[2]) 
        total_cost += nshares * price
    return total_cost

#이후 코드 portfolio의 리스트
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(f)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio


#딕셔너리의 리스트
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2])
            }
            portfolio.append(holding)
    return portfolio