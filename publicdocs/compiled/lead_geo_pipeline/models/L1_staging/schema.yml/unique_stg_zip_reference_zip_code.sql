
    
    

select
    zip_code as unique_field,
    count(*) as n_records

from LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
where zip_code is not null
group by zip_code
having count(*) > 1


