from flask import Blueprint, render_template, request
from app.services.solver import calculate_trajectory

ballistics_bp = Blueprint('ballistics', __name__)

@ballistics_bp.route('/calculate', methods=['POST'])
def calculate():
    initial_velocity = float(request.form['initial_velocity'])
    angle = float(request.form['angle'])
    trajectory = calculate_trajectory(initial_velocity, angle)
    return render_template('results.html', trajectory=trajectory)