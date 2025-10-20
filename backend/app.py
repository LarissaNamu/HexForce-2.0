from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from services.tft_api import get_tft_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

@app.route("/api/tft-data")
def tft_data():
    return get_tft_data()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
