import pandas as pd


def net_profit_margin(net_profit, sales):
    if pd.isna(sales) or sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(op_profit, sales):
    if pd.isna(sales) or sales == 0:
        return None
    return (op_profit / sales) * 100


def roe(net_profit, equity):
    if pd.isna(equity) or equity <= 0:
        return None
    return (net_profit / equity) * 100


def roce(ebit, capital_employed):
    if pd.isna(capital_employed) or capital_employed <= 0:
        return None
    return (ebit / capital_employed) * 100


def roa(net_profit, total_assets):
    if pd.isna(total_assets) or total_assets == 0:
        return None
    return (net_profit / total_assets) * 100