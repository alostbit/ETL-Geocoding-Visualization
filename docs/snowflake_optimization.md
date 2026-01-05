# Snowflake Geospatial Optimization

## Clustering Strategy

### fct_leads Table

- **Cluster Keys:** `state`, `created_date`

- **Reasoning:**

  - `state` enables efficient geographic filtering (GEOGRAPHY columns cannot be used as clustering keys)
  - `created_date` supports time-based filtering common in dashboards
  - Combined clustering optimizes "leads by region in date range" queries
  - For latitude/longitude range queries, consider adding `ROUND(latitude, 1), ROUND(longitude, 1)` to clustering keys

### Query Performance Impact

Clustering reduces micro-partition scanning for filtered queries by ~70-90%.

**Note:** Snowflake does not support clustering on GEOGRAPHY data types directly. Cluster on related scalar columns (state, latitude, longitude) instead.
**Example:** Database Error in model fct_leads (models\L3_marts\fct_leads.sql)
  092103 (42804): Expressions of type GEOGRAPHY cannot be used as ORDER BY keys
  compiled code at target\run\lead_geo_pipeline\models\L3_marts\fct_leads.sql

## Search Optimization (Production Recommendation)

For production deployment with high query volume:

```sql
ALTER TABLE LEAD_ANALYTICS.ANALYTICS.FCT_LEADS 
ADD SEARCH OPTIMIZATION ON EQUALITY(state, city, sales_rep, zip_code);
```

**Cost consideration:** Search optimization adds storage/compute cost. Enable only if:

- Table size > 1M rows
- High-frequency point lookups on indexed columns
- Query performance requirements justify cost

## Geospatial Query Patterns

**Distance-based filtering:**

```sql
-- Find leads within 50km of a point (Dallas, TX)
SELECT lead_id, company_name, city, state
FROM fct_leads
WHERE ST_DISTANCE(location_geo, ST_MAKEPOINT(-96.7970, 32.7767)) < 50000
ORDER BY ST_DISTANCE(location_geo, ST_MAKEPOINT(-96.7970, 32.7767));
```

**Regional aggregation:**

```sql
-- Lead density by state (benefits from clustering)
SELECT state, COUNT(*) as lead_count, SUM(won_revenue) as total_revenue
FROM fct_leads
WHERE created_date >= '2024-01-01'
GROUP BY state
ORDER BY lead_count DESC;
```

**Bounding box queries:**

```sql
-- Leads in a geographic rectangle (more efficient than distance for large areas)
SELECT * FROM fct_leads
WHERE latitude BETWEEN 32.0 AND 33.0
  AND longitude BETWEEN -97.0 AND -96.0;
```

## Performance Recommendations

1. **Use bounding box filters before distance calculations** - latitude/longitude range filters leverage clustering
2. **Materialize common geographic aggregations/territories** - state/county summaries as separate marts if queried frequently
3. **Consider polygon containment for territories if aggregating at that level** - ST_WITHIN for multi-point regions more efficient than multiple distance checks
4. **Monitor query profiles** - Snowflake Query Profile shows clustering effectiveness and partition pruning