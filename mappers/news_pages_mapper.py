from typing import Any
from sqlalchemy import Row, Sequence

from schemas.news_pages_schema import news_pages_schema

class new_pages_mapper:

  def map_rows(self, result: Sequence[Row[Any]]):
    data = []
    for row in result:
      data.append(
        news_pages_schema(row.id, row.name_news_paper, row.url_news_paper).__dict__
      )
        
    return data