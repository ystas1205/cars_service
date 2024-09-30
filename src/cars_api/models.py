from sqlalchemy import Column, Integer, String, Numeric, \
    MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year_of_issue = Column(Integer, nullable=False)
    fuel_type = Column(String(50), nullable=False)
    gearbox_type = Column(String(50), nullable=False)
    mileage = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)