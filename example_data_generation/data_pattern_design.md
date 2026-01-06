# Data Pattern Design for Heatmap Visualization

## Geographic Clustering Patterns by Industry

### Finance
**Primary Markets (60% of leads)**
- New York, NY (Wall Street) - highest deal values
- Chicago, IL (commodities/futures)
- San Francisco, CA (fintech)
- Charlotte, NC (banking HQ)
- Boston, MA (asset management)

**Secondary Markets (30%)**
- Dallas, TX, Atlanta, GA, Philadelphia, PA, Miami, FL

**Characteristics:**
- Deal Value: highest average (200k-1M+)
- Company Size: skewed toward 201-500 and 500+
- Win Rate: moderate (12-15%)
- Sales Cycle: longest (90-180 days)

### Technology
**Primary Markets (50% of leads)**
- San Francisco/San Jose, CA (Silicon Valley)
- Seattle, WA
- Austin, TX
- Boston, MA
- New York, NY

**Secondary Markets (30%)**
- Denver, CO, Portland, OR, Raleigh, NC, Atlanta, GA

**Characteristics:**
- Deal Value: high variance (50k-500k)
- Company Size: bimodal (1-10 startups OR 500+ enterprises)
- Win Rate: moderate-high (15-18%)
- Sales Cycle: medium (60-120 days)

### Healthcare
**Primary Markets (40% of leads)**
- Major metro areas with hospital systems
- Boston, MA (biotech/pharma)
- Houston, TX (medical center)
- Nashville, TN (HCA headquarters)
- Minneapolis, MN (UnitedHealth, Medtronic)
- Philadelphia, PA

**Distributed (60%)**
- More evenly distributed across mid-size cities
- Regional hospital networks

**Characteristics:**
- Deal Value: medium-high (100k-300k)
- Company Size: 51-200 and 201-500 dominant
- Win Rate: high (20-25%) - more stable industry
- Sales Cycle: long (90-150 days) - compliance/procurement

### Retail
**Distribution Pattern:**
- Follows population density
- Concentrated in cities with major retail HQs:
  - Bentonville, AR (Walmart)
  - Minneapolis, MN (Target)
  - Seattle, WA (Amazon)
  - San Francisco, CA (Gap, etc.)
- Otherwise broadly distributed

**Characteristics:**
- Deal Value: medium (25k-100k)
- Company Size: bimodal (small local OR 500+ chains)
- Win Rate: low-medium (10-12%)
- Sales Cycle: short-medium (30-90 days)

### Manufacturing
**Geographic Pattern:**
- Midwest concentration (60%)
  - Detroit, MI area
  - Chicago, IL
  - Milwaukee, WI
  - Indianapolis, IN
  - Cincinnati, OH
  - Pittsburgh, PA
- South (30%)
  - Charlotte, NC, Atlanta, GA, Houston, TX
- Sparse on coasts

**Characteristics:**
- Deal Value: medium-high (75k-250k)
- Company Size: 51-200 and 201-500
- Win Rate: medium (12-15%)
- Sales Cycle: medium-long (75-120 days)

### Professional Services
**Distribution:**
- Follows white-collar job markets
- Major metros: NYC, LA, Chicago, DC, Boston, SF
- Mid-tier cities proportional to population

**Characteristics:**
- Deal Value: low-medium (15k-75k)
- Company Size: 11-50 and 51-200 dominant
- Win Rate: highest (25-30%) - smaller deals, easier to close
- Sales Cycle: shortest (30-60 days)

## Lead Source Geographic Patterns

### Website
- Follows population density
- Slight boost in tech hubs (SF, Seattle, Austin, NYC)

### Cold Outbound
- Concentrated where sales reps are located
- Creates regional clusters around major offices

### Referral
- Higher concentration in established markets
- Clusters around existing customer bases

### Event
- Spiky around major cities with conference centers
- Las Vegas, Orlando, Chicago, San Francisco, New York

### Partner
- Concentrated in partner headquarters locations
- Creates distinct geographic pockets

## Win Rate Geographic Patterns

### High Win Rate Regions (20-25%)
- Established markets where company has presence
- Example clusters:
  - Northeast corridor (if established there)
  - Pacific Northwest
  - Texas triangle (Dallas-Houston-Austin)

### Medium Win Rate Regions (12-15%)
- Growing markets
- Midwest major metros
- Southeast

### Low Win Rate Regions (5-10%)
- Expansion territories
- Rural/sparse areas
- Competitive markets without local presence

## Deal Value Patterns

### High-Value Clusters
- Major metros with Fortune 500 headquarters
- Finance districts: NYC, Chicago, San Francisco
- Tech hubs for technology deals
- Should show as darker/hotter on heatmaps

### Geographic Deal Value Multipliers
- New York, NY: 1.5x
- San Francisco, CA: 1.4x
- Los Angeles, CA: 1.3x
- Chicago, IL: 1.3x
- Boston, MA: 1.25x
- Seattle, WA: 1.25x
- Rural areas: 0.7x
- Small metros: 0.85x

## Sales Rep Territory Patterns

### Alice Chen - West Coast
- CA, OR, WA, NV, AZ
- Highest volume, tech-heavy

### Bob Martinez - Southwest/Mountain
- TX, CO, NM, UT, ID, MT, WY
- Energy, manufacturing focus

### Carol Williams - Midwest
- IL, WI, MI, IN, OH, MN, IA, MO
- Manufacturing, healthcare focus

### David Johnson - Northeast
- NY, MA, PA, NJ, CT, RI, VT, NH, ME
- Finance, professional services focus

### Eva Rodriguez - Southeast
- FL, GA, NC, SC, VA, TN, AL, MS, LA, AR, KY, WV
- Healthcare, retail focus

## Lead Age Patterns

### Newer Leads (<90 days)
- Should cluster in:
  - New expansion markets
  - Recent campaign target areas
  - Post-event locations (if recent events)

### Medium Age (90-365 days)
- Broadly distributed
- Normal pipeline progression

### Old Leads (365+ days)
- Concentrated in:
  - Difficult markets
  - Complex industries (finance, healthcare)
  - Areas with long sales cycles

## Expected Heatmap Highlights

### Revenue Heatmap
**Hotspots:**
- NYC metro (brightest - finance)
- SF Bay Area (bright - tech)
- Chicago (bright - finance/manufacturing)
- LA (medium-bright)
- Boston (medium-bright)

**Medium:**
- Dallas, Houston, Atlanta, Seattle, Denver

**Cool:**
- Rural areas, small metros

### Lead Density Heatmap
**Hotspots:**
- Follows population but with industry bias
- Tech corridor: SF-San Jose
- Finance corridor: NYC-Boston
- Manufacturing belt: Detroit-Chicago-Cleveland

### Win Rate Heatmap
**Hotspots (should be different from revenue):**
- Established territories
- Professional services markets
- Mid-tier cities with less competition

**Cold spots:**
- Highly competitive metros (paradoxically)
- Rural expansion territories
- New markets

### Pipeline Velocity (Days to Close)
**Fast (30-60 days) - should be warm:**
- Professional services markets
- Retail concentrations
- Smaller deal value areas

**Slow (120-180 days) - should be cool:**
- Finance centers
- Healthcare hubs
- Large enterprise concentrations

## Data Generation Strategy

1. **Create industry-specific ZIP probability distributions**
   - Weight ZIPs by industry headquarters and market presence

2. **Apply deal value multipliers**
   - Based on metro area, industry, company size

3. **Set realistic win rates**
   - By territory, industry, lead source

4. **Create temporal patterns**
   - Seasonal variations
   - Campaign-driven spikes in specific regions

5. **Territory assignment logic**
   - Assign sales rep based on state/region
   - Create rep performance variance

## Key Metrics for Variation

### By Geography
- Lead volume variance: 50x between hottest and coolest metros
- Deal value variance: 5x between regions
- Win rate variance: 5x between territories

### By Industry
- Finance: lowest volume, highest value, longest cycle
- Professional Services: highest volume, lowest value, shortest cycle
- Technology: high variance in all metrics

### By Sales Rep
- Performance variance: 1.5x between best and worst
- Volume variance: territory-dependent
- Win rate should vary by rep skill AND territory difficulty
