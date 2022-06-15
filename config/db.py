from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root@localhost:3306/ft")
Base = declarative_base()

Session = sessionmaker(engine)



