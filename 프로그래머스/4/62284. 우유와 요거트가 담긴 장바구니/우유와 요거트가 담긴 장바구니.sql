#Cart products에서 milk가 있는 테이블을 가져와서 yogurt를 포함한 cart id 출력하기
SELECT CART_ID
FROM CART_PRODUCTS
WHERE CART_ID IN 
      (SELECT CART_ID
      FROM CART_PRODUCTS
      WHERE NAME = 'Yogurt'
      ) AND
      CART_ID IN
      (SELECT CART_ID
      FROM CART_PRODUCTS
      WHERE NAME ='Milk'
      )
GROUP BY CART_ID


