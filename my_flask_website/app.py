from flask import Flask, render_template

app = Flask(__name__)

# Existing routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

# Blog post routes
@app.route('/blog/post1')
def post1():
    return render_template('post1.html')

@app.route('/blog/post2')
def post2():
    return render_template('post2.html')

@app.route('/blog/post3')
def post3():
    return render_template('post3.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

if __name__ == '__main__':
    app.run(debug=True)
