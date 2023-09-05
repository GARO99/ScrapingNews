from app import app
from flask import request

@app.route("/news", methods=["GET"])
def get_news_by_topic():
  topic = request.args['topic']
  return topic