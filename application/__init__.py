from flask import Flask, render_template, send_from_directory

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        socials = [
            ("https://www.instagram.com/octaveatlanta/"),("Instagram-Logo.png"),
        ]
        return render_template('coming_soon.html', sm_accts=socials)

    @app.route('/robots.txt')
    def robots():
        return send_from_directory(app.static_folder,"robots.txt")

    return app