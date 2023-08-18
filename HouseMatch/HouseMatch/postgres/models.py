from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.dialects.postgresql import BOOLEAN

Base = declarative_base()

class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    date = Column(Date, nullable=True)
    location_site = Column(String, nullable=True)
    category_site = Column(String, nullable=True)
    area = Column(Integer, nullable=True)
    post_type = Column(String, nullable=True)
    room_count = Column(Integer, nullable=True)
    parking = Column(String, nullable=True)
    mortgage = Column(Float, nullable=True)
    rent = Column(Float, nullable=True)
    elevator = Column(String, nullable=True)
    warehouse = Column(String, nullable=True)
    age = Column(Integer, nullable=True)

    def __str__(self):
        return (
            f"House(id={self.id}, title={self.title}, price={self.price}, "
            f"date={self.date}, location_site={self.location_site}, "
            f"category_site={self.category_site}, area={self.area}, "
            f"post_type={self.post_type}, room_count={self.room_count}, "
            f"parking={self.parking}, mortgage={self.mortgage}, "
            f"rent={self.rent}, elevator={self.elevator}, "
            f"warehouse={self.warehouse}, age={self.age})"
        )