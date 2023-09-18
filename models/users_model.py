from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from DbContext.mysql_context import get_conection, meta

users_model = Table(
  "users",
  meta,
  Column("id", Integer, nullable=False, primary_key=True, autoincrement=True),
  Column("user_name", String(45), nullable=False),
  Column("email", String(100), nullable=False),
  Column("password", String(64), nullable=False),
)

meta.create_all(get_conection())