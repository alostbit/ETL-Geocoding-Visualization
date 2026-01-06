WITH leads AS (
    SELECT * FROM {{ ref('stg_leads') }}
),

geo AS (
    SELECT * FROM {{ ref('stg_zip_reference') }}
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
        -- Add US Census region classification
        CASE
            WHEN g.state IN ('CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA') THEN 'Northeast'
            WHEN g.state IN ('IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD') THEN 'Midwest'
            WHEN g.state IN ('DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX', 'DC') THEN 'South'
            WHEN g.state IN ('AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA') THEN 'West'
            ELSE 'Other'
        END AS region,
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