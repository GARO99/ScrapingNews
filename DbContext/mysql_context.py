from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@127.0.0.1:3306/scrapingnews")

meta = MetaData()

dbConnection = engine.connect()