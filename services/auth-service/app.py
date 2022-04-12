from auth_service.server import create_app

app = create_app()
application = app

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
