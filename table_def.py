# table_def.py
from sqlalchemy import ForeignKey, Sequence
from sqlalchemy import Column, Date, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

 
#use these to create tabels from scratch
#engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()
 
 
########################################################################
class client(Base):
    """
    client table
    """
    __tablename__ = "client"
    #primary key
    client_id = Column(Integer, Sequence('client_id_seq'), primary_key=True)   
    
    first_name = Column(String)  
    last_name = Column(String)     
    dob = Column(Date) 
    phone_number = Column(String)    
    account = Column(String)

 
    #----------------------------------------------------------------------
    def __init__(self, client_id, first_name, last_name, dob, phone_number, account):
        """"""
        self.client_id = client_id
        self.first_name = first_name  
        self.last_name = last_name   
        self.dob = dob
        self.phone_number = phone_number    
        self.account = account

########################################################################
class act_log(Base):
    """
    activity log table
    """
    __tablename__ = "act_log"
    # handel our ids and foreign relationships
    #primary key
    transaction_id = Column(Integer, Sequence('client_id_seq'), primary_key=True) 
    #forgein key client
    client_id = Column(Integer, ForeignKey('client.client_id'))
    client = relationship("client", backref=backref("client", order_by=client_id))
    # forein key contact
    provider_id = Column(Integer, ForeignKey('contact.provider_id'))
    contact = relationship("contact", backref=backref("contact", order_by=provider_id))
    
    date = Column(Date)    
    descp = Column(Text)   
    descp_cat = Column(Text)   
    time = Column(Float)    
    unit_price = Column(Integer) 
    total = Column(Integer) 
 
    #----------------------------------------------------------------------
    def __init__(self, transaction_id, client_id, date, descp, descp_cat, time, unit_price, total):
        """

        """
        self.transaction_id = transaction_id 
        self.client_id = client_id
        self.date = date    
        self.descp = descp   
        self.descp_cat = descp_cat 
        self.time = time   
        self.unit_price = unit_price
        self.total = total

class contact(Base):
    """
    activity log table
    """
    __tablename__ = 'contact'
    # handel our ids and foreign relationships
    #primary key
    provider_id = Column(Integer, Sequence('provider_id_seq'), primary_key=True) 
    #forgein key client
    client_id = Column(Integer, ForeignKey('client.client_id'))
    #client = relationship("client", backref=backref("client", order_by=client_id))
    # forein key contact
    # can add transacton id in the future
    
    PROVIDER_NAME = Column(Text)    
    SPECIALITY = Column(Text)   
    PHONE = Column(Text)   
    CONTACT_NAME = Column(Text)    
    ADDRESS = Column(Text) 
    MISC = Column(Text) 
    Miles = Column(Float) 
 
    #----------------------------------------------------------------------
    def __init__(
                    self, provider_id, client_id, PROVIDER_NAME, SPECIALITY, PHONE, 
                    CONTACT_NAME, ADDRESS, MISC, Miles):
        """

        """
        self.provider_id = provider_id
        self.client_id = client_id
        self.PROVIDER_NAME = PROVIDER_NAME 
        self.SPECIALITY = SPECIALITY
        self.PHONE = PHONE    
        self.CONTACT_NAME = CONTACT_NAME   
        self.ADDRESS = ADDRESS 
        self.MISC = MISC   
        self.Miles = Miles

