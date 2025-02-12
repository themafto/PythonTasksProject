SELECT
    o.order_id,
    o.item,
    o.amount,
    o.customer_id,
    s.status
FROM Orders o
JOIN Shippings s ON o.customer_id = s.customer;
                                                      -- то оно просто не присоеденит в таблицу товар, который уже существует к примеру? не могу до конца разобраться.