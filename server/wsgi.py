from flask import Flask

app = Flask(__name__)

# Import your application routes and models here
# For example:
# from my_app.routes import main_routes
# from my_app.models import db

# Initialize your application components
# For example:
# db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)