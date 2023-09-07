class news_pages_schema:
  id: int
  name_news_paper: str
  url_news_paper: str
  
  def __init__(self, id, name_news_paper, url_news_paper):
    self.id = id
    self.name_news_paper = name_news_paper
    self.url_news_paper = url_news_paper
    
  def __getattr__(self, attr):
    return self[attr]