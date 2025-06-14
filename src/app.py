import os
import requests
import random
import datetime
from flask import Flask, send_from_directory, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
  # return list of endpoints with links and documentation
  documentation = f"""
  <font face="Open Sans"><h2>Hello World!</h2>
  <a href="/">/</a> - This documentation page<br>
  <a href="/test">/test</a> - Returns current timestamp in ISO format and a random number (1-100)<br>
  <a href="/wikipedia">/wikipedia</a> - Fetches and returns https://www.wikipedia.com/ content<br>
  <a href="/time">/time</a> - Fetches current time from https://time.now<br>
  </font>
  """
  return documentation

@app.route('/test')
def test():
  # Return random number with ISO datetime (YYYY-MM-DD HH:MM:SS)
  try:
    iso_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Timestamp: {iso_datetime}<br>\n Random Number: {str(random.randint(1, 100))}", 200 
  except Exception as e: 
    return f"Error: {e}", 500

@app.route('/wikipedia')
def wikipedia():
  try: return requests.get("https://www.wikipedia.com/").text, 200 
  except Exception as e: return f"Error: {e}", 500
  
@app.route('/time')
def time():
  try: return requests.get("https://time.now/").text, 200 
  except Exception as e: return f"Error: {e}", 500

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',      # Required for Azure
    port=int(os.environ.get('PORT', 5000)),
    debug=False           # Disable debug mode in production
  )
