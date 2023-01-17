from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

messages = []


@app.route('/dictionary')
def dictionary():
    # Your dictionary
    return jsonify(messages)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print(request.form['name'])
        return redirect(url_for('message', name=request.form['name'], _method='GET'))
    elif request.method == 'GET':
        return render_template('index.html')
    else:
        print(request.method)


@app.route('/message/<name>', methods=['GET', 'POST'])
def message(name):
    if request.method == 'POST':
        print(request.form)
        try:
            messages.append([name,request.form['message']])
        except:
            print("no message")
        return redirect(url_for('message', name=name, _method='GET'))
    elif request.method == 'GET':
        print("GET")
        return render_template('message.html', name=name, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
