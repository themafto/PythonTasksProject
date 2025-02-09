SELECT
    Customers.customer_id,
    Customers.first_name,
    Customers.last_name,
    Orders.item,
    Orders.amount
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
