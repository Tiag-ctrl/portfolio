from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__,template_folder='template')
app.run(debug=True)



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")



@app.route("/perfil", methods=["GET"])
def perfil():
    return render_template("perfil.html")



@app.route("/atividades", methods=["GET"])
def atividades():
    return render_template("atividades.html")

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

app.run(debug=True)