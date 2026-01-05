
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select zip_code
from LEAD_ANALYTICS.ANALYTICS.stg_leads
where zip_code is null



  
  
      
    ) dbt_internal_test