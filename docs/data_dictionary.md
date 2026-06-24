# Data Dictionary

## fund_master.csv
- amfi_code : Unique mutual fund identifier
- fund_house : Fund company name
- scheme_name : Scheme name
- category : Fund category
- risk_category : Risk level

## nav_history.csv
- amfi_code : Fund identifier
- date : NAV date
- nav : Net Asset Value

## investor_transactions.csv
- investor_id : Investor ID
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount
- state : Investor state
- kyc_status : KYC verification status

## scheme_performance.csv
- return_1yr_pct : 1 year return
- return_3yr_pct : 3 year return
- return_5yr_pct : 5 year return
- sharpe_ratio : Risk adjusted return
- expense_ratio_pct : Expense ratio