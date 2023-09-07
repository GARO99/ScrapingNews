from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

from Controllers import news_controller

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify({"error": "Bad Request", "message": str(error)})
    response.status_code = 400  # Establecer el código de estado HTTP a 400
    return response

@app.errorhandler(Exception)
def handle_exception(e):
  response = jsonify({"message": "An error occurred", "error": str(e)})
  response.status_code = 500
  return response

if __name__ == '__main__':
  app.run(debug=True)