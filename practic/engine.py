from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/practic")

Base = declarative_base()

session = Session(bind = engine)
print("Connected to the database")