from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def render_page(page_name):
    return render_template(page_name)

if __name__ == "__main__":
    app.run(debug=True)
