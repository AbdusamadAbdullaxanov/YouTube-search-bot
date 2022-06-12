from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine

CONNECTION = "postgresql://postgres:postgresql@localhost/FastAPI"
engine = create_engine(CONNECTION)
Session = sessionmaker(bind=engine)
Base = declarative_base(engine)
