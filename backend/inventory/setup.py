import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory.database import db_session
from inventory.models import User

# Set up database
from inventory.database import init_db
init_db()

# Add some dummy data

# Categories

# u = User('julian', 'julz@localhost')
# db_session.add(u)
# db_session.commit()

