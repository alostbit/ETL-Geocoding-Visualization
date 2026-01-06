
  create or replace   view LEAD_ANALYTICS.ANALYTICS.stg_zip_reference
  
  
  
  
  as (
    WITH source AS (
    SELECT * FROM LEAD_ANALYTICS.ANALYTICS.uszips
),

cleaned AS (
    SELECT
        LPAD(zip, 5, '0') AS zip_code,
        city,
        state_id AS state,
        county_name AS county,
        lat AS latitude,
        lng AS longitude
    FROM source
    WHERE zip IS NOT NULL
)

SELECT * FROM cleaned
  );

