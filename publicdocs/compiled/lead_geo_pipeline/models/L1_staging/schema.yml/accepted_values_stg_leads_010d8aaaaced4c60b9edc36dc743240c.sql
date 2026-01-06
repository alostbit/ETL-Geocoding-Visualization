
    
    

with all_values as (

    select
        lead_status as value_field,
        count(*) as n_records

    from LEAD_ANALYTICS.ANALYTICS.stg_leads
    group by lead_status

)

select *
from all_values
where value_field not in (
    'New','Qualified','Opportunity','Won','Lost'
)


