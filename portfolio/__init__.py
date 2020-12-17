from flask import Flask, render_template

app = Flask(__name__) #create new instance of flask
@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
