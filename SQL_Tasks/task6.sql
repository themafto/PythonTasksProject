SELECT DISTINCT(c.first_name), c.last_name, s.status
FROM Customers c
LEFT JOIN Shippings s ON c.customer_id = s.customer
WHERE status = 'Delivered'