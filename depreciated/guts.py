# queries.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import act_log, client
 
engine = create_engine('sqlite:///CRM.sqlite', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# how to do a SELECT * (i.e. all)
res = session.query(act_log).all()
for log in res:
    print act_log.date
 
# # how to SELECT the first result
# res = session.query(Artist).filter(Artist.name=="Newsboys").first()
 
# # how to sort the results (ORDER_BY)
# res = session.query(Album).order_by(Album.title).all()
# for album in res:
#     print album.title
 
# # how to do a JOINed query
# qry = session.query(Artist, Album)
# qry = qry.filter(Artist.id==Album.artist_id)
# artist, album = qry.filter(Album.title=="Thrive").first()
# print
 
# # how to use LIKE in a query
# res = session.query(Album).filter(Album.publisher.like("S%a%")).all()
# for item in res:
#     print item.publisher
