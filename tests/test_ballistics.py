import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.services.solver import calculate_trajectory

class BallisticsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_calculate_trajectory(self):
        trajectory = calculate_trajectory(100, 45)
        self.assertIsInstance(trajectory, list)
        self.assertGreater(len(trajectory), 0)

    def test_calculate_route(self):
        response = self.client.post('/calculate', data={
            'initial_velocity': 100,
            'angle': 45
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ballistics Calculator - Results', response.data)

if __name__ == '__main__':
    unittest.main()
