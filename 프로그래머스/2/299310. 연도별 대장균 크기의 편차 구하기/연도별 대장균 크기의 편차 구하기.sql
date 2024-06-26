-- 코드를 작성해주세요
# SELECT  (Max(C.SIZE_OF_COLONY)-P.SIZE_OF_COLONY) AS YEAR_DEV, P.ID, DIFFERENTIATION_DATE
# FROM ECOLI_DATA AS P
# LEFT JOIN ECOLI_DATA AS C
# ON C.PARENT_ID = P.ID
# GROUP BY P.DIFFERENTIATION_DATE

SELECT B.YEAR, B.SIZE_OF_COLONY-D.SIZE_OF_COLONY AS YEAR_DEV, D.ID
FROM
(SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS SIZE_OF_COLONY
FROM ECOLI_DATA
GROUP BY YEAR(DIFFERENTIATION_DATE)) AS B
RIGHT JOIN (
    SELECT ID, PARENT_ID, SIZE_OF_COLONY, YEAR(DIFFERENTIATION_DATE) AS YEAR, GENOTYPE
    FROM ECOLI_DATA
    ) AS D
ON D.YEAR=B.YEAR
ORDER BY 1, 2


