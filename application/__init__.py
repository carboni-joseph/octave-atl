from flask import Flask, render_template

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        socials = [
            ("https://www.instagram.com/octaveatlanta/"),("Instagram-Logo.png"),
        ]
        return render_template('coming_soon.html', sm_accts=socials)

    return app