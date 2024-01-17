from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Handle Get/POSt requests to web app
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_question = request.form['question']
        ai_answer = getAnswer(user_question)
        return render_template('index.html', question = user_question, answer = ai_answer)

# Use transforer model to get answer from earth.txt context
def getAnswer(question):
    # load pipeline
    qa_model = pipeline("question-answering", "bert-large-uncased-whole-word-masking-finetuned-squad")

    # read context from earth.txt
    f = open("earth.txt", "r")
    context = f.read()

    result = qa_model(question = question, context = context)
    answer = result["answer"].capitalize() + "." # punctuate the sentance

    return answer

# Default model:
# distilbert-base-cased-distilled-squad

# Another model
# bert-large-uncased-whole-word-masking-finetuned-squad