SELECT COUNT(A.ID) AS FISH_COUNT
FROM (SELECT ID, CASE WHEN LENGTH IS NULL THEN 0 ELSE LENGTH END LENGTH
     FROM FISH_INFO
     ) A
WHERE A.LENGTH <= 10