from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    if session.get('counter') is not None:
        session['counter'] += 1
        print session['counter']
    else:
        session['counter'] = 0
        print session['counter']
    return render_template('index.html') 

@app.route('/forward', methods=['GET'])
def add_two():
    session['counter'] += 2
    return render_template('index.html')

@app.route('/reset', methods=['GET'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)