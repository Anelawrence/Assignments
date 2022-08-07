-- SQLite
SELECT item,quantity,price,
CASE 
WHEN quantity > 25 THEN 'Sufficient'
ELSE 'Not sufficient'
END AS 'Quantity status'
FROM stock
ORDER BY price DESC;



SELECT SUM(price) 
FROM stock;

SELECT AVG(quantity) 
FROM stock;

SELECT item, MIN(quantity) 
FROM stock;

SELECT item, MAX(quantity) 
FROM stock;