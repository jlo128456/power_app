from models import Base, engine, SessionLocal, EnergyPlan

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Sample energy plans
sample_plans = [
    {
        "provider": "AGL",
        "plan_name": "AGL Value Saver",
        "postcode": "2000",
        "state": "NSW",
        "usage_rate_cents": 25.3,
        "supply_charge_cents": 98.5,
        "solar_feed_in_cents": 6.0,
        "contract_length_months": 12,
        "green_energy_percent": 20,
        "fact_sheet_url": "https://agl.com.au/factsheets/value-saver"
    },
    {
        "provider": "Origin",
        "plan_name": "Origin Go Plan",
        "postcode": "3000",
        "state": "VIC",
        "usage_rate_cents": 23.9,
        "supply_charge_cents": 95.0,
        "solar_feed_in_cents": 5.5,
        "contract_length_months": 12,
        "green_energy_percent": 25,
        "fact_sheet_url": "https://origin.com.au/factsheets/go-plan"
    },
    {
        "provider": "EnergyAustralia",
        "plan_name": "Total Plan Home",
        "postcode": "4000",
        "state": "QLD",
        "usage_rate_cents": 24.7,
        "supply_charge_cents": 90.0,
        "solar_feed_in_cents": 7.0,
        "contract_length_months": 24,
        "green_energy_percent": 15,
        "fact_sheet_url": "https://energyaustralia.com.au/factsheets/total-home"
    },
    {
        "provider": "Red Energy",
        "plan_name": "Living Energy Saver",
        "postcode": "2000",
        "state": "NSW",
        "usage_rate_cents": 26.5,
        "supply_charge_cents": 101.0,
        "solar_feed_in_cents": 5.0,
        "contract_length_months": 24,
        "green_energy_percent": 100,
        "fact_sheet_url": "https://redenergy.com.au/factsheets/living-saver"
    },
    {
        "provider": "Powershop",
        "plan_name": "Smart Saver",
        "postcode": "6000",
        "state": "WA",
        "usage_rate_cents": 25.0,
        "supply_charge_cents": 92.0,
        "solar_feed_in_cents": 8.0,
        "contract_length_months": 6,
        "green_energy_percent": 50,
        "fact_sheet_url": "https://powershop.com.au/factsheets/smart-saver"
    },
    {
        "provider": "Lumo Energy",
        "plan_name": "Lumo Advantage",
        "postcode": "5000",
        "state": "SA",
        "usage_rate_cents": 27.1,
        "supply_charge_cents": 89.5,
        "solar_feed_in_cents": 6.2,
        "contract_length_months": 12,
        "green_energy_percent": 15,
        "fact_sheet_url": "https://lumoenergy.com.au/factsheets/advantage"
    },
    {
        "provider": "Alinta Energy",
        "plan_name": "HomeDeal",
        "postcode": "3000",
        "state": "VIC",
        "usage_rate_cents": 24.3,
        "supply_charge_cents": 87.5,
        "solar_feed_in_cents": 6.5,
        "contract_length_months": 12,
        "green_energy_percent": 10,
        "fact_sheet_url": "https://alintaenergy.com.au/factsheets/homedeal"
    },
    {
        "provider": "Simply Energy",
        "plan_name": "Simply Basics",
        "postcode": "4000",
        "state": "QLD",
        "usage_rate_cents": 23.8,
        "supply_charge_cents": 93.0,
        "solar_feed_in_cents": 5.8,
        "contract_length_months": 18,
        "green_energy_percent": 20,
        "fact_sheet_url": "https://simplyenergy.com.au/factsheets/basics"
    },
    {
        "provider": "Dodo Power",
        "plan_name": "Dodo Simple Plan",
        "postcode": "2000",
        "state": "NSW",
        "usage_rate_cents": 25.9,
        "supply_charge_cents": 88.0,
        "solar_feed_in_cents": 6.9,
        "contract_length_months": 6,
        "green_energy_percent": 0,
        "fact_sheet_url": "https://dodo.com.au/factsheets/simple-plan"
    },
    {
        "provider": "ReAmped Energy",
        "plan_name": "ReAmped Handshake",
        "postcode": "5000",
        "state": "SA",
        "usage_rate_cents": 22.5,
        "supply_charge_cents": 85.0,
        "solar_feed_in_cents": 7.5,
        "contract_length_months": 1,
        "green_energy_percent": 100,
        "fact_sheet_url": "https://reampedenergy.com.au/factsheets/handshake"
    }
]

# Insert sample plans into the database
session = SessionLocal()
for plan_data in sample_plans:
    plan = EnergyPlan(**plan_data)
    session.add(plan)

session.commit()
session.close()

print("Seeded 10 mock energy plans into database.db.")
