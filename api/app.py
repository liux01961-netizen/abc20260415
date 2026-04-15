from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 確保這行存在，給 Vercel 呼叫
app = app