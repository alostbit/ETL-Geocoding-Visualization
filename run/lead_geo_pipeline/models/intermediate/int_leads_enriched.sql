
  create or replace   view LEAD_ANALYTICS.ANALYTICS.int_leads_enriched
  
  
  
  
  as (
    WITH leads AS (
    SELECT * FROM LEAD_ANALYTICS.ANALYTICS.stg_leads
),

geo AS (
    SELECT * FROM LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
),

enriched AS (
    SELECT
        l.lead_id,
        l.company_name,
        l.zip_code,
        g.city,
        g.state,
        g.county,
        g.latitude,
        g.longitude,
        -- Create Snowflake GEOGRAPHY point
        ST_MAKEPOINT(g.longitude, g.latitude) AS location_geo,
        l.lead_source,
        l.lead_status,
        l.industry,
        l.company_size,
        l.deal_value,
        l.sales_rep,
        l.created_date,
        l.close_date,
        -- Calculated fields
        DATEDIFF(day, l.created_date, CURRENT_DATE()) AS lead_age_days,
        DATEDIFF(day, l.created_date, l.close_date) AS days_to_close
    FROM leads l
    LEFT JOIN geo g ON l.zip_code = g.zip_code
)

SELECT * FROM enriched
  );

