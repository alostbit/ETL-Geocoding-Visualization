
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

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



  
  
      
    ) dbt_internal_test