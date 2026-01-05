
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select location_geo
from LEAD_ANALYTICS.ANALYTICS.fct_leads
where location_geo is null



  
  
      
    ) dbt_internal_test