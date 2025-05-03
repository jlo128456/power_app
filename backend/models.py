from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# Create base class for models
Base = declarative_base()

# Connect to SQLite database
DATABASE_URL = 'sqlite:///energy.db'
engine = create_engine(DATABASE_URL, echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Energy Plan model
class EnergyPlan(Base):
    __tablename__ = 'energy_plans'

    id = Column(Integer, primary_key=True)
    provider = Column(String, nullable=False)
    plan_name = Column(String, nullable=False)
    postcode = Column(String, nullable=False)
    state = Column(String, nullable=False)
    usage_rate_cents = Column(Float, nullable=False)
    supply_charge_cents = Column(Float, nullable=False)
    solar_feed_in_cents = Column(Float)
    contract_length_months = Column(Integer)
    green_energy_percent = Column(Integer)
    fact_sheet_url = Column(Text)
