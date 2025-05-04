# Entry point and backend server file for Flask
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import db, EnergyPlan, User
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

# Get all energy plans
@app.route('/api/energy-plans')
def get_energy_plans():
    try:
        plans = EnergyPlan.query.all()
        return jsonify([plan.to_dict() for plan in plans]), 200
    except SQLAlchemyError:
        return jsonify(error="Failed to fetch energy plans"), 500

# Create a new user
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        user = User(
            username=data['username'],
            password=data['password'],
            postcode=data['postcode']
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except (KeyError, SQLAlchemyError):
        return jsonify(error="Invalid user data or database error"), 400

# Get plans by user's postcode
@app.route('/api/energy-plans-by-postcode/<postcode>')
def get_plans_by_postcode(postcode):
    postcode_group = map_postcode_to_group(postcode)
    try:
        plans = EnergyPlan.query.filter_by(postcode_group=postcode_group).all()
        if not plans:
            return jsonify(error="No plans found for that postcode"), 404
        return jsonify([plan.to_dict() for plan in plans]), 200
    except SQLAlchemyError:
        return jsonify(error="Database error"), 500

# Map postcode to group based on first digit
def map_postcode_to_group(postcode):
    if not postcode or not postcode.isdigit():
        return "4000"
    first_digit = postcode[0]
    return {
        "2": "2000",
        "3": "3000",
        "4": "4000",
        "6": "6000"
    }.get(first_digit, "4000")

# Global error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Resource not found"), 404

# Global error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify(error="Internal server error"), 500

# Run the server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
