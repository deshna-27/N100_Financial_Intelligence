def debt_to_equity(total_debt, equity):
    if equity == 0:
        return None
    return round(total_debt / equity, 2)


def interest_coverage(ebit, interest):
    if interest == 0:
        return None
    return round(ebit / interest, 2)


def net_debt(total_debt, cash):
    return total_debt - cash


def asset_turnover(revenue, assets):
    if assets == 0:
        return None
    return round(revenue / assets, 2)