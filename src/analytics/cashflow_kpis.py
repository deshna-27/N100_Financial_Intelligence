def free_cash_flow(operating_cf, capex):
    """
    Free Cash Flow = Operating Cash Flow - Capital Expenditure
    """
    return operating_cf - capex


def cashflow_quality(operating_cf, net_profit):
    """
    Cash Flow Quality = Operating Cash Flow / Net Profit
    """
    if net_profit == 0:
        return None

    return round(operating_cf / net_profit, 2)


def capex_intensity(capex, revenue):
    """
    CapEx Intensity = CapEx / Revenue
    """
    if revenue == 0:
        return None

    return round(capex / revenue, 2)


def fcf_conversion(fcf, operating_cf):
    """
    FCF Conversion = Free Cash Flow / Operating Cash Flow
    """
    if operating_cf == 0:
        return None

    return round(fcf / operating_cf, 2)