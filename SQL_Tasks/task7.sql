SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.amount) AS total_amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY o.amount DESC
LIMIT 1;

