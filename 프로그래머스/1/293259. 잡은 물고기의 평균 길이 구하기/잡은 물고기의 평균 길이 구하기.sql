-- 코드를 작성해주세요
SELECT ROUND(AVG(FISH_INFO.LENGTH),2) AS AVERAGE_LENGTH
FROM 
(SELECT COALESCE(LENGTH, 10) AS LENGTH
FROM FISH_INFO) AS FISH_INFO

