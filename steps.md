# Snowflake Setup

In Worksheet
CREATE DATABASE LEAD_ANALYTICS;

USE DATABASE LEAD_ANALYTICS;

CREATE SCHEMA RAW;
CREATE SCHEMA STAGING;
CREATE SCHEMA ANALYTICS;

pip install dbt-snowflake

create dbt directory, profiles.yml within it

cd into that directory

dbt init lead_geo_pipeline

press 1 to select snowflake connection

enter prompts

cd to project (cd lead_geo_pipeline)

dbt debug

pip install faker

create folder for faker script
create data subfolder in that folder

run script

download zip database https://simplemaps.com/data/us-zips

zip csv into lead_geo_pipeline/seeds (create if not present)

cd lead_geo_pipeline
run dbt seed

OR use AirByte (Ignoring for now)

copy faker generated raw_leads.csv to other seeds location

cd into lead_geo_pipeline

run dbt seed --select raw_leads

DATA UPLOADED, MODELING NEEDED
Model 1: stg_leads.sql
What it does:
Takes raw_leads seed data
Fixes ZIP code formatting (pads to 5 digits: "1234" → "01234")
Converts date strings to proper DATE types
Standardizes column names (if needed)

Create the file:
mkdir models/staging (if not present)

The SQL breakdown:

{{ ref('raw_leads') }} - dbt magic: references the seed, handles schema automatically
LPAD(zip_code, 5, '0') - ensures all ZIPs are 5 characters (critical for JOIN later)
CTEs (WITH statements) - readable, testable structure