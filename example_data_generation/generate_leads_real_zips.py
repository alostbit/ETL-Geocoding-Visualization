from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker('en_US')
Faker.seed(42)

# Load real ZIPs from reference data
print("Loading valid ZIP codes...")
zip_ref = pd.read_csv('lead_geo_pipeline/seeds/uszips.csv')
valid_zips = zip_ref['zip'].astype(str).str.zfill(5).tolist()
print(f"Loaded {len(valid_zips)} valid ZIP codes")

# Configuration
NUM_LEADS = 20000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

LEAD_SOURCES = ['Website', 'Referral', 'Cold Outbound', 'Event', 'Partner', 'Content']
LEAD_STATUSES = ['New', 'Qualified', 'Opportunity', 'Won', 'Lost']
INDUSTRIES = ['Technology', 'Professional Services', 'Manufacturing', 'Healthcare', 'Retail', 'Finance', 'Other']
COMPANY_SIZES = ['1-10', '11-50', '51-200', '201-500', '500+']
SALES_REPS = ['Alice Chen', 'Bob Martinez', 'Carol Williams', 'David Johnson', 'Eva Rodriguez']

leads = []

for i in range(NUM_LEADS):
    lead_id = f"LEAD-{i+1:06d}"
    company = fake.company()
    zip_code = random.choice(valid_zips)  # Use real ZIPs
    
    source = random.choices(LEAD_SOURCES, weights=[30, 25, 15, 15, 10, 5])[0]
    status = random.choices(LEAD_STATUSES, weights=[20, 25, 30, 15, 10])[0]
    industry = random.choice(INDUSTRIES)
    company_size = random.choices(COMPANY_SIZES, weights=[15, 30, 30, 15, 10])[0]
    sales_rep = random.choice(SALES_REPS)
    
    # Deal value based on company size
    size_multipliers = {'1-10': 5000, '11-50': 15000, '51-200': 50000, '201-500': 150000, '500+': 500000}
    base_value = size_multipliers[company_size]
    deal_value = int(random.gauss(base_value, base_value * 0.3))
    deal_value = max(1000, deal_value)
    
    # Created date
    created_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE)
    
    # Close date logic
    if status in ['Won', 'Lost']:
        days_to_close = random.randint(30, 180)
        close_date = created_date + timedelta(days=days_to_close)
        if close_date > END_DATE:
            close_date = None
    else:
        close_date = None
    
    leads.append({
        'lead_id': lead_id,
        'company_name': company,
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

df = pd.DataFrame(leads)
df.to_csv('example_data_generation/data/raw_leads.csv', index=False)
print(f"Generated {NUM_LEADS} leads")
print(f"\nSample data:")
print(df.head())
print(f"\nLead status distribution:")
print(df['lead_status'].value_counts())
print(f"\nUnique ZIP codes used: {df['zip_code'].nunique()}")