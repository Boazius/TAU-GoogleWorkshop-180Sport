from flask_sqlalchemy import SQLAlchemy
from application import create_app
from models import User
from models import User_type
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
import os


app = create_app()
# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="919619848127-0d5ata8oi64g4neesm7vss0cb30evnph.apps.googleusercontent.com",
    client_secret="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",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)
db = SQLAlchemy(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    # app.run(debug=True)
