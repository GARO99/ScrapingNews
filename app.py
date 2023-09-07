from flask import Flask

app = Flask(__name__)

try:
    from Controllers import *
except Exception as e:
    print(e)

@app.errorhandler(Exception)
def handle_exception(e):
  response = {
    "code": e.code,
    "name": e.name,
    "description": e.description,
  }
  
  return response, response["code"]

if __name__ == '__main__':
  app.run(debug=True)