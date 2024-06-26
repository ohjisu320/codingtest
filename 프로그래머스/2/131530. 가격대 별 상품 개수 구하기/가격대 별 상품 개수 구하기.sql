SELECT 
CASE 
    WHEN LENGTH(PRICE)<5 THEN 0
    WHEN LENGTH(PRICE)=5 THEN LEFT(PRICE,1)*10000
END AS PRICE_GROUP, COUNT(DISTINCT PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY 1
ORDER BY 1
