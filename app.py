
from flask import Flask, render_template
app = Flask (__name__)	

#Pagina Principal
@app.route('/')
def inicio():
    return render_template("principal.html")


app.run(debug=True)
