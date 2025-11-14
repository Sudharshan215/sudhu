SELECT
    c.name AS customer_name,
    c.email,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    pay.amount AS payment_amount,
    pay.payment_method
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN payments pay ON o.order_id = pay.order_id
LIMIT 20;