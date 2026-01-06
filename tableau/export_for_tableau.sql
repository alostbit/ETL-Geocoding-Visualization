-- Query to export FCT_LEADS data with properly formatted geography for Tableau
-- Run this in Snowflake and download the results as CSV

SELECT
    lead_id,
    company_name,
    zip_code,
    city,
    state,
    county,
    latitude,
    longitude,
    -- Format GEOGRAPHY as single-line GeoJSON string
    TO_VARCHAR(ST_ASGEOJSON(location_geo)) AS location_geojson,
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
    pipeline_stage,
    is_won,
    won_revenue
FROM LEAD_ANALYTICS.ANALYTICS.FCT_LEADS;

-- Alternative: Use WKT format instead of GeoJSON
-- Replace the location_geojson line with:
-- ST_ASWKT(location_geo) AS location_wkt,
