from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

fake = Faker('en_US')
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Load real ZIPs with geographic info
print("Loading valid ZIP codes...")
zip_ref = pd.read_csv('zip_data/uszips.csv')
zip_ref['zip'] = zip_ref['zip'].astype(str).str.zfill(5)
print(f"Loaded {len(zip_ref)} valid ZIP codes")

# Configuration
NUM_LEADS = 140000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 1, 5)

LEAD_SOURCES = ['Website', 'Referral', 'Cold Outbound', 'Event', 'Partner', 'Content']
LEAD_STATUSES = ['New', 'Qualified', 'Opportunity', 'Won', 'Lost']
INDUSTRIES = ['Technology', 'Professional Services', 'Manufacturing', 'Healthcare', 'Retail', 'Finance', 'Other']
COMPANY_SIZES = ['1-10', '11-50', '51-200', '201-500', '500+']

# Sales rep territories
SALES_REPS = {
    'Alice Chen': ['CA', 'OR', 'WA', 'NV', 'AZ', 'HI', 'AK'],
    'Bob Martinez': ['TX', 'CO', 'NM', 'UT', 'ID', 'MT', 'WY', 'OK', 'KS', 'NE', 'SD', 'ND'],
    'Carol Williams': ['IL', 'WI', 'MI', 'IN', 'OH', 'MN', 'IA', 'MO'],
    'David Johnson': ['NY', 'MA', 'PA', 'NJ', 'CT', 'RI', 'VT', 'NH', 'ME', 'DE', 'MD', 'DC'],
    'Eva Rodriguez': ['FL', 'GA', 'NC', 'SC', 'VA', 'TN', 'AL', 'MS', 'LA', 'AR', 'KY', 'WV']
}

# Major metro areas by industry focus
INDUSTRY_METROS = {
    'Finance': {
        'primary': [('NY', 0.25), ('IL', 0.15), ('CA', 0.10), ('NC', 0.10), ('MA', 0.10)],
        'cities': ['New York', 'Chicago', 'San Francisco', 'Charlotte', 'Boston', 'Philadelphia', 'Dallas', 'Miami']
    },
    'Technology': {
        'primary': [('CA', 0.35), ('WA', 0.15), ('TX', 0.10), ('MA', 0.08), ('NY', 0.07)],
        'cities': ['San Francisco', 'San Jose', 'Seattle', 'Austin', 'Boston', 'New York', 'Denver', 'Portland']
    },
    'Healthcare': {
        'primary': [('MA', 0.12), ('TX', 0.10), ('TN', 0.08), ('MN', 0.08), ('PA', 0.08)],
        'cities': ['Boston', 'Houston', 'Nashville', 'Minneapolis', 'Philadelphia', 'Baltimore', 'Cleveland']
    },
    'Retail': {
        'primary': [('AR', 0.10), ('MN', 0.10), ('WA', 0.08), ('CA', 0.08)],
        'cities': ['Bentonville', 'Minneapolis', 'Seattle', 'San Francisco', 'Atlanta', 'Chicago']
    },
    'Manufacturing': {
        'primary': [('MI', 0.15), ('IL', 0.12), ('OH', 0.12), ('IN', 0.10), ('WI', 0.08)],
        'cities': ['Detroit', 'Chicago', 'Milwaukee', 'Indianapolis', 'Cincinnati', 'Pittsburgh', 'Cleveland']
    },
    'Professional Services': {
        'primary': [('NY', 0.15), ('CA', 0.15), ('IL', 0.10), ('TX', 0.10), ('MA', 0.08)],
        'cities': None  # follows general population
    },
    'Other': {
        'primary': [],
        'cities': None
    }
}

# Deal value base by industry and company size
DEAL_VALUE_BASE = {
    'Finance': {'1-10': 50000, '11-50': 150000, '51-200': 400000, '201-500': 800000, '500+': 2000000},
    'Technology': {'1-10': 30000, '11-50': 100000, '51-200': 300000, '201-500': 600000, '500+': 1500000},
    'Healthcare': {'1-10': 40000, '11-50': 120000, '51-200': 250000, '201-500': 500000, '500+': 1000000},
    'Manufacturing': {'1-10': 25000, '11-50': 75000, '51-200': 200000, '201-500': 450000, '500+': 900000},
    'Retail': {'1-10': 15000, '11-50': 40000, '51-200': 100000, '201-500': 250000, '500+': 600000},
    'Professional Services': {'1-10': 10000, '11-50': 30000, '51-200': 75000, '201-500': 150000, '500+': 350000},
    'Other': {'1-10': 15000, '11-50': 45000, '51-200': 120000, '201-500': 250000, '500+': 500000}
}

# Metro area deal value multipliers
METRO_MULTIPLIERS = {
    'New York': 1.5, 'San Francisco': 1.4, 'San Jose': 1.4, 'Los Angeles': 1.3,
    'Chicago': 1.3, 'Boston': 1.25, 'Seattle': 1.25, 'Washington': 1.2,
    'Dallas': 1.15, 'Houston': 1.15, 'Atlanta': 1.1, 'Miami': 1.1
}

# Company size distribution by industry
COMPANY_SIZE_DIST = {
    'Finance': [5, 15, 25, 30, 25],  # skewed large
    'Technology': [25, 25, 20, 15, 15],  # bimodal
    'Healthcare': [10, 20, 35, 25, 10],  # mid-size heavy
    'Manufacturing': [10, 25, 35, 20, 10],  # mid-size heavy
    'Retail': [20, 20, 20, 20, 20],  # bimodal
    'Professional Services': [15, 35, 30, 15, 5],  # small-mid heavy
    'Other': [20, 30, 30, 15, 5]
}

# Win rate by industry
WIN_RATES = {
    'Finance': 0.12,
    'Technology': 0.16,
    'Healthcare': 0.22,
    'Manufacturing': 0.14,
    'Retail': 0.11,
    'Professional Services': 0.28,
    'Other': 0.15
}

# Sales cycle days by industry
SALES_CYCLE = {
    'Finance': (90, 180),
    'Technology': (60, 120),
    'Healthcare': (90, 150),
    'Manufacturing': (75, 120),
    'Retail': (30, 90),
    'Professional Services': (30, 60),
    'Other': (45, 90)
}

def get_zip_for_industry(industry):
    """Select ZIP code based on industry clustering patterns"""
    industry_info = INDUSTRY_METROS.get(industry, INDUSTRY_METROS['Other'])

    # 60% chance to use primary markets for focused industries
    if industry_info['primary'] and random.random() < 0.6:
        # Select state based on weights
        states, weights = zip(*industry_info['primary'])
        state = random.choices(states, weights=weights)[0]
        state_zips = zip_ref[zip_ref['state_id'] == state]

        # Within state, bias toward major cities if specified
        if industry_info['cities']:
            city_zips = state_zips[state_zips['city'].isin(industry_info['cities'])]
            if len(city_zips) > 0 and random.random() < 0.7:
                return city_zips.sample(1).iloc[0]

        return state_zips.sample(1).iloc[0]

    # Otherwise, random selection with population weighting
    # Larger population ZIPs are more likely
    weights = zip_ref['population'].fillna(1) + 1
    return zip_ref.sample(1, weights=weights).iloc[0]

def assign_sales_rep(state):
    """Assign sales rep based on territory"""
    for rep, states in SALES_REPS.items():
        if state in states:
            return rep
    return random.choice(list(SALES_REPS.keys()))

def calculate_deal_value(industry, company_size, city, population):
    """Calculate deal value with industry, size, geographic, and population multipliers"""
    base = DEAL_VALUE_BASE[industry][company_size]

    # Apply metro multiplier
    city_multiplier = METRO_MULTIPLIERS.get(city, 1.0)

    # Apply population-based multiplier (with diminishing returns)
    # Log scale so it doesn't dominate, with randomness
    if population and population > 0:
        # Normalize: typical ZIP has 10k-50k people
        # Small ZIP (5k): ~0.85x, Medium (30k): ~1.0x, Large (100k): ~1.15x
        pop_factor = np.log10(population + 1) / np.log10(30000)
        pop_multiplier = 0.85 + (pop_factor - 1) * 0.3
        # Add randomness to population effect (50% weight on population, 50% random)
        pop_multiplier = pop_multiplier * 0.5 + random.uniform(0.8, 1.2) * 0.5
    else:
        pop_multiplier = 1.0

    # Combine multipliers
    total_multiplier = city_multiplier * pop_multiplier

    # Add final randomness
    value = int(random.gauss(base * total_multiplier, base * total_multiplier * 0.25))
    return max(1000, value)

# Generate leads
print(f"Generating {NUM_LEADS} leads with realistic patterns...")
leads = []

for i in range(NUM_LEADS):
    # Select industry
    industry = random.choice(INDUSTRIES)

    # Select ZIP based on industry
    zip_row = get_zip_for_industry(industry)
    zip_code = zip_row['zip']
    city = zip_row['city']
    state = zip_row['state_id']

    # Assign sales rep by territory
    sales_rep = assign_sales_rep(state)

    # Company size based on industry distribution
    company_size = random.choices(COMPANY_SIZES, weights=COMPANY_SIZE_DIST[industry])[0]

    # Calculate deal value (pass population from zip_row)
    population = zip_row['population'] if pd.notna(zip_row['population']) else 0
    deal_value = calculate_deal_value(industry, company_size, city, population)

    # Lead source and status
    source = random.choices(LEAD_SOURCES, weights=[30, 25, 15, 15, 10, 5])[0]

    # Determine status based on industry win rate
    win_rate = WIN_RATES[industry]
    rand_val = random.random()
    if rand_val < win_rate:
        status = 'Won'
    elif rand_val < win_rate + 0.08:
        status = 'Lost'
    elif rand_val < win_rate + 0.08 + 0.25:
        status = 'Opportunity'
    elif rand_val < win_rate + 0.08 + 0.25 + 0.20:
        status = 'Qualified'
    else:
        status = 'New'

    # Created date with some temporal variance
    # Create seasonal patterns - more leads in Q1 and Q4
    month_weights = [12, 10, 8, 7, 7, 6, 6, 7, 8, 9, 11, 12]  # Jan-Dec
    days_in_period = (END_DATE - START_DATE).days
    random_days = random.randint(0, days_in_period)
    created_date = START_DATE + timedelta(days=random_days)

    # Close date logic
    if status in ['Won', 'Lost']:
        cycle_min, cycle_max = SALES_CYCLE[industry]
        days_to_close = random.randint(cycle_min, cycle_max)
        close_date = created_date + timedelta(days=days_to_close)
        if close_date > END_DATE:
            close_date = END_DATE - timedelta(days=random.randint(1, 30))
    else:
        close_date = None

    leads.append({
        'lead_id': f"LEAD-{i+1:06d}",
        'company_name': fake.company(),
        'zip_code': zip_code,
        'lead_source': source,
        'lead_status': status,
        'industry': industry,
        'company_size': company_size,
        'deal_value': deal_value,
        'sales_rep': sales_rep,
        'created_date': created_date.strftime('%Y-%m-%d'),
        'close_date': close_date.strftime('%Y-%m-%d') if close_date else None
    })

    if (i + 1) % 10000 == 0:
        print(f"Generated {i + 1} leads...")

df = pd.DataFrame(leads)

# Save to CSV
output_path = 'lead_geo_pipeline/seeds/raw_leads.csv'
df.to_csv(output_path, index=False)

print(f"\nGenerated {NUM_LEADS} leads")
print(f"Saved to {output_path}")
print(f"\nData Summary:")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Memory: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")

print(f"\nLead status distribution:")
print(df['lead_status'].value_counts())

print(f"\nIndustry distribution:")
print(df['industry'].value_counts())

print(f"\nSales rep distribution:")
print(df['sales_rep'].value_counts())

print(f"\nTop 10 states by lead volume:")
state_counts = df.merge(zip_ref[['zip', 'state_id']], left_on='zip_code', right_on='zip', how='left')
print(state_counts['state_id'].value_counts().head(10))

print(f"\nDeal value statistics:")
print(df['deal_value'].describe())

print(f"\nWin rate by industry:")
won_by_industry = df[df['lead_status'] == 'Won'].groupby('industry').size()
total_by_industry = df.groupby('industry').size()
win_rates = (won_by_industry / total_by_industry * 100).round(1)
print(win_rates.sort_values(ascending=False))
