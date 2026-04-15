from flask import Flask, render_template, url_for

# 這裡不變
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 改成這樣，確保 Vercel 能抓到
app = app