# table_def.py
from sqlalchemy import create_engine, ForeignKey, Sequence
from sqlalchemy import Column, Date, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

 
#use these to create tabels from scratch
#engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()
 
 
########################################################################
class client(Base):
    """"""
    __tablename__ = "client"
    
    client_id = Column(Integer, Sequence('client_id_seq'), primary_key=True)   
    first_name = Column(String)  
    last_name = Column(String)     
    dob = Column(Date) 
    phone_number = Column(String)    
    account = Column(String)

 
    #----------------------------------------------------------------------
    def __init__(self, client_id, first_name,  last_name,   dob, phone_number,    account):
        """"""
        self.client_id = client_id
        self.first_name = first_name  
        self.last_name = last_name   
        self.dob = dob
        self.phone_number = phone_number    
        self.account = account

########################################################################
class act_log(Base):
    """"""
    __tablename__ = "act_log"
   
    transaction_id = Column(Integer, Sequence('client_id_seq'), primary_key=True) 
    
    client_id = Column(Integer, ForeignKey("client.client_id"))
    client = relationship("client", backref=backref("client", order_by=client_id))
    
    date = Column(Date)    
    descp = Column(Text)   
    descp_cat = Column(Text)   
    time = Column(Float)    
    unit_price = Column(Integer) 
    total = Column(Integer) 
 
    #----------------------------------------------------------------------
    def __init__(self, transaction_id, client_id, date, descp, descp_cat, time, unit_price, total):
        """"""
        self.transaction_id = transaction_id 
        self.client_id = client_id
        self.date = date    
        self.descp = descp   
        self.descp_cat = descp_cat 
        self.time = time   
        self.unit_price = unit_price
        self.total = total
