SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COALESCE(SUM(o.amount), 0) AS total_amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.customer_id;




