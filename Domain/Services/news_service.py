import bs4 as bs
import requests
from urllib.parse import urlparse
from tqdm import tqdm
import urllib3
from DbContext.mysql_context import dbConnection
from mappers.news_pages_mapper import new_pages_mapper
from models.news_pages_model import news_pages_model
from schemas.news_pages_schema import news_pages_schema

class News_service:  
  def __init__(self):
    self.mapper = new_pages_mapper()
    self.data = []
  
  def get_available_news_papers(self):
    result = dbConnection.execute(
        news_pages_model.select()
      ).fetchall()
    
    return self.mapper.map_rows(result)
  
  def scrape_news_by_topic(self, topic: str):
    self.data = []
    for news_pepers in self.get_available_news_papers():
      news = news_pages_schema(**news_pepers)
      html_page = self._get_webpage(news.url_news_paper)
      self._search_topic_on_news_page(html_page, topic, news.url_news_paper)
    
    return self.data
  
  def _get_webpage(self, url):
    response = requests.get(url)
    return response.text
  
  def _search_topic_on_news_page(self, html_page, topic, newspaper_url):
    soup = bs.BeautifulSoup(html_page, 'lxml')
    table = soup.find('div')
    if table:
      for row in tqdm(soup.findAll('h2')):
        if row.findAll('a') and row.find_all('a') and  row.find_next('p'):            
          title = row.findAll('a')[0].text
          link = row.find_all('a')[0].get("href")
          content = row.find_next('p').text
          if topic.lower() in title.lower() or topic.lower() in content.lower():
            parsed_url = urlparse(link)
            is_not_relative_url = bool(parsed_url.scheme)
            self.data.append(
              {
                "title": title,
                "link": link if is_not_relative_url  else newspaper_url+link
              }
            )
    
    return self.data
          