import sys
import os
import string
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory.database import db_session
from inventory.models import *

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Set up database
from inventory.database import init_db
init_db()

# Add some dummy data
for i in range(5):
    category = Category(generate_random_string(), generate_random_string())
    db_session.add(category)
    db_session.commit()

