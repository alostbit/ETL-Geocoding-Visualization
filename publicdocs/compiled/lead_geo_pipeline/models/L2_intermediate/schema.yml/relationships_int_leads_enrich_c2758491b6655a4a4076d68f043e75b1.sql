
    
    

with child as (
    select zip_code as from_field
    from LEAD_ANALYTICS.ANALYTICS.int_leads_enriched
    where zip_code is not null
),

parent as (
    select zip_code as to_field
    from LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


