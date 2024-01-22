from app import app, db

def create_app():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
