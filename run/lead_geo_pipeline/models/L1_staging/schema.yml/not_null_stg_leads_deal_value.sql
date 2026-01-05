
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select deal_value
from LEAD_ANALYTICS.ANALYTICS.stg_leads
where deal_value is null



  
  
      
    ) dbt_internal_test