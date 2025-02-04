from flask_migrate import Migrate
from backend.api import create_app
from backend.api.models.db import db

app = create_app()
Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)