select count(*) FISH_COUNT, b.FISH_NAME
from fish_info a join fish_name_info b on a.fish_type = b.fish_type
group by b.fish_name
order by FISH_COUNT desc;