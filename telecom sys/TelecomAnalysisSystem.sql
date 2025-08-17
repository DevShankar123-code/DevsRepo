Create database Telecom_Industry_Analysis;
use Telecom_Industry_Analysis;
-- KEY RESPONSIBILITY AREA 1(Data Cleaning & PreProcessing )
SELECT COUNT(*) FROM telecom_customers_churn;
-- Check for missing values in important columns
SELECT 
    SUM(CASE WHEN MonthlyCharges IS NULL THEN 1 ELSE 0 END) AS Missing_MonthlyCharges,
    SUM(CASE WHEN TotalCharges IS NULL THEN 1 ELSE 0 END) AS Missing_TotalCharges,
    SUM(CASE WHEN Tenure IS NULL THEN 1 ELSE 0 END) AS Missing_Tenure
FROM telecom_customers_churn;

-- Check for duplicate customer IDs
SELECT CustomerID, COUNT(*) 
FROM telecom_customers_churn 
GROUP BY CustomerID 
HAVING COUNT(*) > 1;

-- Key Responsibility Area 3 (Customers Patterns & Trands).
-- Churn count by contract type
SELECT Contract, COUNT(*) AS Total, 
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned
FROM telecom_customers_churn
GROUP BY Contract;

-- Average tenure of churned vs non-churned customers
SELECT Churn, ROUND(AVG(Tenure), 2) AS Avg_Tenure
FROM telecom_customers_churn
GROUP BY Churn;

-- Most used internet service
SELECT InternetService, COUNT(*) AS Users
FROM telecom_customers_churn
GROUP BY InternetService
ORDER BY Users DESC;

-- Key Responsibility Area 4(SQL Queries For Data Extraction)..
-- Customers with high monthly charges (> ₹90)
SELECT CustomerID, MonthlyCharges, Churn
FROM telecom_customers_churn
WHERE MonthlyCharges > 90;

-- Customers who use both StreamingTV and StreamingMovies
SELECT CustomerID, StreamingTV, StreamingMovies
FROM telecom_customers_churn
WHERE StreamingTV = 'Yes' AND StreamingMovies = 'Yes';

-- Count of customers by payment method
SELECT PaymentMethod, COUNT(*) AS Total_Customers
FROM telecom_customers_churn
GROUP BY PaymentMethod;

-- Key Responsibility Area 5 (A/B Testing)..
-- Churn rate for Month-to-Month vs Long-Term contracts
SELECT Contract,
       COUNT(*) AS Total_Customers_churn,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
       ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telecom_customers_churn
GROUP BY Contract;

-- Key Responsibily Area 9 (Promotional Insights)
-- Region-wise churn rate
-- Customers with Tenure < 6 Months and High Monthly Charges..
SELECT customerID, tenure, MonthlyCharges, Contract
FROM telecom_customers_churn
WHERE tenure < 6 AND MonthlyCharges > 80;

-- Churn Rate by Contract Type (to target retention offers)
SELECT 
    Contract,
    COUNT(*) AS Total_Customers_churn,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telecom_customers_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;

-- Customers Using Both StreamingTV and StreamingMovies.
SELECT customerID, StreamingTV, StreamingMovies, InternetService
FROM telecom_customers_churn
WHERE StreamingTV = 'Yes' AND StreamingMovies = 'Yes';

-- Customers with DSL Internet and High Charges
SELECT customerID, InternetService, MonthlyCharges
FROM telecom_customers_churn
WHERE InternetService = 'DSL' AND MonthlyCharges > 80;

-- Key Responsibility Area 10(KPI Tracking)
-- Retained customers (non-churned) with long tenure
SELECT CustomerID, Tenure
FROM telecom_customers_churn
WHERE Churn = 'No' AND Tenure > 24;

-- ROI proxy: TotalCharges vs MonthlyCharges
SELECT CustomerID, MonthlyCharges, TotalCharges,
       ROUND(TotalCharges / MonthlyCharges, 2) AS ROI_Months
FROM telecom_customers_churn
WHERE MonthlyCharges > 0;