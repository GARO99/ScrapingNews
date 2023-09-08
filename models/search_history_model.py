from sqlalchemy import ForeignKeyConstraint, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from DbContext.mysql_context import get_conection, meta

search_history_model = Table(
  "search_history",
  meta,
  Column("id", Integer, nullable=False, primary_key=True, autoincrement=True),
  Column("topic", String(45), nullable=False),
  Column("users_id", Integer, nullable=False),
  ForeignKeyConstraint(
    ["users_id"], 
    ["users.id"],
    name="fk_search_history_users_id"
  )
)

meta.create_all(get_conection())