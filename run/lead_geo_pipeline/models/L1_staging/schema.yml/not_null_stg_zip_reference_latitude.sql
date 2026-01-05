
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select latitude
from LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
where latitude is null



  
  
      
    ) dbt_internal_test