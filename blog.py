from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def first():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/watch_that_starts_it_all')
def post_one():
    return render_template('post_one.html')

@app.route('/SNK809')
def post_two():
    return render_template('post_two.html')

@app.route('/SKX013')
def post_three():
    return render_template('post_three.html')

@app.route('/speedy_pro')
def post_four():
    return render_template('post_four.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)