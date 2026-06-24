-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav
FROM nav_history;

-- 3. Average NAV per Fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- 4. Total SIP Inflow
SELECT SUM(sip_inflow_crore) AS total_sip
FROM monthly_sip_inflows;

-- 5. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 7. Top Categories by Inflow
SELECT category, SUM(net_inflow_crore) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

-- 8. Highest 5-Year Returns
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 9. Investor Count by Age Group
SELECT age_group, COUNT(*) AS investors
FROM investor_transactions
GROUP BY age_group;

-- 10. Fund House AUM Ranking
SELECT fund_house, MAX(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;