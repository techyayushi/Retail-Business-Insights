-- =====================================================
-- Retail Business Insights - SQL Analysis
-- Database: retail_business
-- =====================================================

USE retail_business;

-- 1. View the complete dataset
SELECT * FROM retail_cleaned;

-- =====================================================
-- KPI ANALYSIS
-- =====================================================

-- 2. Total Sales, Profit, Orders & Customers
SELECT
    ROUND(SUM(Sales),2) AS Total_Sales,
    ROUND(SUM(Profit),2) AS Total_Profit,
    COUNT(Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM retail_cleaned;

-- =====================================================
-- SALES ANALYSIS
-- =====================================================

-- 3. Sales by Category
SELECT
    Category,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_cleaned
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 4. Profit by Region
SELECT
    Region,
    ROUND(SUM(Profit),2) AS Total_Profit
FROM retail_cleaned
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 5. Sales by Customer Segment
SELECT
    Segment,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_cleaned
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- 6. Top 10 Products by Sales
SELECT
    Product_Name,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_cleaned
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 7. Top 10 Cities by Sales
SELECT
    City,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_cleaned
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 10;

-- =====================================================
-- PROFIT ANALYSIS
-- =====================================================

-- 8. Profit by Category
SELECT
    Category,
    ROUND(SUM(Profit),2) AS Total_Profit
FROM retail_cleaned
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 9. Profit by Customer Segment
SELECT
    Segment,
    ROUND(SUM(Profit),2) AS Total_Profit
FROM retail_cleaned
GROUP BY Segment
ORDER BY Total_Profit DESC;

-- 10. Profit Margin by Category
SELECT
    Category,
    ROUND(SUM(Sales),2) AS Sales,
    ROUND(SUM(Profit),2) AS Profit,
    ROUND((SUM(Profit)/SUM(Sales))*100,2) AS Profit_Margin_Percentage
FROM retail_cleaned
GROUP BY Category
ORDER BY Profit_Margin_Percentage DESC;

-- 11. Profit Margin by Region
SELECT
    Region,
    ROUND(SUM(Sales),2) AS Sales,
    ROUND(SUM(Profit),2) AS Profit,
    ROUND((SUM(Profit)/SUM(Sales))*100,2) AS Profit_Margin_Percentage
FROM retail_cleaned
GROUP BY Region
ORDER BY Profit_Margin_Percentage DESC;

-- =====================================================
-- CUSTOMER INSIGHTS
-- =====================================================

-- 12. Top 10 Customers by Sales
SELECT
    Customer_ID,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_cleaned
GROUP BY Customer_ID
ORDER BY Total_Sales DESC
LIMIT 10;

-- 13. Customer Distribution by Segment
SELECT
    Segment,
    COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM retail_cleaned
GROUP BY Segment
ORDER BY Total_Customers DESC;

-- =====================================================
-- TIME TREND ANALYSIS
-- =====================================================

-- 14. Monthly Sales & Profit Trend
SELECT
    DATE_FORMAT(Order_Date,'%Y-%m') AS Month,
    ROUND(SUM(Sales),2) AS Total_Sales,
    ROUND(SUM(Profit),2) AS Total_Profit,
    COUNT(Order_ID) AS Total_Orders
FROM retail_cleaned
GROUP BY DATE_FORMAT(Order_Date,'%Y-%m')
ORDER BY Month;