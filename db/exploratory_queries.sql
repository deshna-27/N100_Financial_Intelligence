-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Top 10 companies by ROE
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- 3. Top 10 companies by ROCE
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- 4. Highest stock closing price
SELECT company_id,
MAX(close_price) AS highest_close
FROM stock_prices;

-- 5. Total stock records
SELECT COUNT(*)
FROM stock_prices;

-- 6. Number of balance sheet records
SELECT COUNT(*)
FROM balancesheet;

-- 7. Number of profit & loss records
SELECT COUNT(*)
FROM profitandloss;

-- 8. Number of cashflow records
SELECT COUNT(*)
FROM cashflow;

-- 9. Companies with ROE greater than 20%
SELECT company_name, roe_percentage
FROM companies
WHERE roe_percentage > 20;

-- 10. Average ROE
SELECT AVG(roe_percentage)
FROM companies;