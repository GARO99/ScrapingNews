from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from DbContext.mysql_context import get_conection, meta

news_pages_model = Table(
  "news_pages", 
  meta,
  Column("id", Integer, nullable=False, primary_key=True, autoincrement=True),
  Column("name_news_paper", String(45), nullable=False),
  Column("url_news_paper", String(250), nullable=False)
)

meta.create_all(get_conection())