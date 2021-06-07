from flask import Flask, render_template, request

app = Flask(__name__)

task = []
@app.route('/', methods=["GET","POST"])
def index():
    if request.method=='POST':
        note = request.form.get("note")
        task.append(note)
    return render_template("home.html", notes=task)


if __name__ == '__main__':
    app.run(debug=True)