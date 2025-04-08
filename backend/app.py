from flask import Flask, request
from flask_cors import CORS
from routes import mortgage_routes

app = Flask(__name__)
CORS(app)

# Debug log 
@app.before_request
def log_request_info():
    print("🔵 Request Method:", request.method)
    print("🔵 Request URL:", request.url)
    print("🔵 Request Headers:", dict(request.headers))
    print("🔵 Request Body:", request.get_data(as_text=True))

app.register_blueprint(mortgage_routes)

if __name__ == "__main__":
    app.run(debug=True)
