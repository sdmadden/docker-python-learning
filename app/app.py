import os
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.sep, 'app', 'settings', 'default_settings.cfg'))
app.config.from_pyfile(os.path.join(os.sep, 'app', 'settings', 'environment_settings.cfg'), silent=True)

@app.route('/')
def hello_world():
    return f'Hello, world! {app.config["DATABASE_CONNECTION"]}\n'
