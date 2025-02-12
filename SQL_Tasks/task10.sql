SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.age,
    COALESCE(o.item, 'No order') AS item,
    o.amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE age = (SELECT MIN(age) FROM Customers)