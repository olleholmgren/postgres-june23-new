from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db

db = create_engine("postgresql:///chinook")