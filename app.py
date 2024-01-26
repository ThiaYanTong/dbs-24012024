from flask import Flask
app = Flask(__name__)
from flask import request, render_template
@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html", result = (rate*-50.6)+90.2))
    else:
        return render_template("index.html", result ="Waiting……….")
if __name__=="__main__":
    app.run()
