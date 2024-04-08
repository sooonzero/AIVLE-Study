-- 비트 연산을 활용해서 푸는방법
-- 좋은 풀이라 생각해서 가져왔다.
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 5 AND NOT GENOTYPE & 2
