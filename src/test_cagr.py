from analytics.cagr import *

print("Revenue CAGR:", revenue_cagr(100, 200, 5))
print("Profit CAGR :", profit_cagr(50, 100, 5))
print("EPS CAGR    :", eps_cagr(10, 20, 5))

print("Zero Start  :", revenue_cagr(0, 100, 5))
print("Negative    :", revenue_cagr(-50, 100, 5))