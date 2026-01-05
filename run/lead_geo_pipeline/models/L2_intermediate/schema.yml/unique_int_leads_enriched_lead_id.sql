
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    lead_id as unique_field,
    count(*) as n_records

from LEAD_ANALYTICS.ANALYTICS.int_leads_enriched
where lead_id is not null
group by lead_id
having count(*) > 1



  
  
      
    ) dbt_internal_test