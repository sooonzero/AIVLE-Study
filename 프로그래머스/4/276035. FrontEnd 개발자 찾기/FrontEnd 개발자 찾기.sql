select distinct(b.ID), b.EMAIL, b.FIRST_NAME, b.LAST_NAME
from (select code
    from skillcodes
    where category = 'Front End') a, developers b
where b.skill_code & (a.code)
ORDER BY ID;