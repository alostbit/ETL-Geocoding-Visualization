WITH source AS (
    SELECT * FROM LEAD_ANALYTICS.ANALYTICS.raw_leads
),

cleaned AS (
    SELECT
        lead_id,
        company_name,
        LPAD(zip_code, 5, '0') AS zip_code,  -- Pads ZIP: "1234" becomes "01234"
        lead_source,
        lead_status,
        industry,
        company_size,
        deal_value,
        sales_rep,
        TO_DATE(created_date) AS created_date,
        TO_DATE(close_date) AS close_date
    FROM source
)

SELECT * FROM cleaned