-- SQLite
SELECT item,quantity,price,
CASE 
WHEN quantity > 25 THEN 'Sufficient'
ELSE 'Not sufficient'
END AS 'Quantity status'
FROM stock
ORDER BY price DESC;