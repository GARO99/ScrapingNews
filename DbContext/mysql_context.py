from sqlalchemy import create_engine, MetaData

meta = MetaData()

def get_conection():
  return create_engine("mysql+pymysql://root@127.0.0.1:3306/scrapingnews")