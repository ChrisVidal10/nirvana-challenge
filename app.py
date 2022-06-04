from src import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app("flask.cfg")

# Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
