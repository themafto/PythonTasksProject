SELECT
    o.order_id,
    o.item,
    o.amount,
    c.customer_id,
    s.status
FROM Orders o
INNER JOIN Customers c ON o.customer_id = c.customer_id
LEFT JOIN Shippings s ON o.customer_id = s.customer;  -- тут же должен быть LEFT вместо INNER, ибо если записей в SHipping нету,
                                                      -- то оно просто не присоеденит в таблицу товар, который уже существует к примеру? не могу до конца разобраться.