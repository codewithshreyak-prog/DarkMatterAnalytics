-- Top 10 customers by number of orders

SELECT customer_id,
       COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;


-- Top 10 customers by revenue

SELECT o.customer_id,
       SUM(oi.revenue) AS total_revenue
FROM orders o
JOIN order_items oi
ON o.invoice_no = oi.invoice_no
GROUP BY o.customer_id
ORDER BY total_revenue DESC
LIMIT 10;


-- Top 10 products by revenue

SELECT stock_code,
       SUM(revenue) AS total_revenue
FROM order_items
GROUP BY stock_code
ORDER BY total_revenue DESC
LIMIT 10;


-- Monthly order trend

SELECT DATE_TRUNC('month', invoice_date) AS month,
       COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;