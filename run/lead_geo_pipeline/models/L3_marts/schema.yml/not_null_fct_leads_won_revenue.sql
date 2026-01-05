
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select won_revenue
from LEAD_ANALYTICS.ANALYTICS.fct_leads
where won_revenue is null



  
  
      
    ) dbt_internal_test