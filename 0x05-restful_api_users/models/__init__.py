#!/usr/bin/python3
"""
module containing database config
"""

import os
from models.base_model import Base, BaseModel
from models.user import User
from models.user_session import UserSession
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

db_config = {'drivername': 'mysql+mysqldb',
             'username': os.getenv('HBNB_YELP_MYSQL_USER'),
             'password': os.getenv('HBNB_YELP_MYSQL_PWD'),
             'host': os.getenv('HBNB_YELP_MYSQL_HOST'),
             'database': os.getenv('HBNB_YELP_MYSQL_DB')}

db_engine = create_engine(URL(**db_config))

if db_config['database'] == 'hbtn_yelp_test':
    Base.metadata.drop_all(bind=db_engine)

Base.metadata.create_all(db_engine)

db_session = scoped_session(sessionmaker(bind=db_engine,
                                         expire_on_commit=False))
