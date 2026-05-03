from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_articles():
    return [
        {
            'link_herf':'http://www.google.come',
            'image_src': 'static/images/image1.jpg',
            
                            }
    ]

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)

