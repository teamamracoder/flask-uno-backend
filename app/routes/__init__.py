from .user_routes import user_bp

blueprints = [user_bp]

def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)