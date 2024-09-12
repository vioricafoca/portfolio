import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/blog")
def blog():
    return render_template('index1.html')

if __name__ == "__main__":
    app.run(debug=True)


