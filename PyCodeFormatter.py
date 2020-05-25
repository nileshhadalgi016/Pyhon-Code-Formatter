from flask import Flask, render_template, request
import autopep8
import pyperclip
from flaskwebgui import FlaskUI

app = Flask(__name__)
#ui = FlaskUI(app)


@app.route("/")
def index_page():
    return render_template("index.html", pycode='Lets beautify your code.', row=10)


@app.route("/formatter", methods=['POST', 'GET'])
def formatter():
    if request.method == 'POST':
        pycode = request.form['pycode']
        button = request.form['submit']
        pycode = autopep8.fix_code(pycode, options={'aggressive': 2})
        row = len(pycode.split('\n'))
        if button == 'format':
            return render_template("index.html", pycode=pycode, row=row)
        if button == 'formatandcopytoclipboard':
            pyperclip.copy(pycode)
            return render_template("index.html",
                                   pycode="Copied to clipboard.Just carry the code safely and past it at the destination.",
                                   row=5)

if __name__ == '__main__':
    #ui.run()
    app.run(debug=True)
