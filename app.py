from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes

# Init app
app = Flask(__name__)

# Init flask restful
api = Api(app)

# Init resources endpoints
initialize_routes(api)

# Run Server
if __name__ == '__main__':
  app.run()
