{{
  config(
    materialized='table',
    cluster_by=['state', 'created_date']
  )
}}

WITH enriched AS (
    SELECT * FROM {{ ref('int_leads_enriched') }}
),

final AS (
    SELECT
        lead_id,
        company_name,
        zip_code,
        city,
        state,
        county,
        latitude,
        longitude,
        location_geo,
        lead_source,
        lead_status,
        industry,
        company_size,
        deal_value,
        sales_rep,
        created_date,
        close_date,
        lead_age_days,
        days_to_close,
        -- Derived flags for dashboard filtering
        CASE 
            WHEN lead_status IN ('Won', 'Lost') THEN 'Closed'
            ELSE 'Active'
        END AS pipeline_stage,
        CASE 
            WHEN lead_status = 'Won' THEN 1
            ELSE 0
        END AS is_won,
        -- Revenue fields
        CASE 
            WHEN lead_status = 'Won' THEN deal_value
            ELSE 0
        END AS won_revenue
    FROM enriched
)

SELECT * FROM final