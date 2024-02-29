SELECT A.DEPT_ID, A.DEPT_NAME_EN, ROUND(AVG(SAL),0) AVG_SAL
FROM HR_DEPARTMENT A JOIN HR_EMPLOYEES B
ON A.DEPT_ID = B.DEPT_ID
GROUP BY 1
ORDER BY 3 DESC;