from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        ai_answer = "This is your answer!"
        return render_template('index.html', answer = ai_answer)

