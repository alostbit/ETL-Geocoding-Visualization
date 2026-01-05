
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select longitude
from LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
where longitude is null



  
  
      
    ) dbt_internal_test