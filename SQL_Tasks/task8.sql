SELECT
	c.country,
	COUNT(*) AS pending_shipments
FROM Customers c
LEFT JOIN Shippings s ON c.customer_id = s.customer
WHERE status = 'Pending'
GROUP BY s.customer