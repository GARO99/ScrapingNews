from app import app
from flask import jsonify, request
from Domain.Services.news_service import News_service

service = News_service() 

@app.route("/news", methods=["GET"])
def get_news_by_topic():
  return service.scrape_news_by_topic(request.args['topic'])

@app.route("/news/available", methods=["GET"])
def get_available_news_papers(): 
  return jsonify(service.get_available_news_papers())