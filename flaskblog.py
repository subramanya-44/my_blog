from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'subramanya',
        'title': 'notes from underground',
        'content': 'on hollow men',
        'date_posted': 'jan 20, 12024'
    },
    {
        'author': 'ram',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'feb 10, 12024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
