
from flask import Flask, render_template
app = Flask (__name__)	

#Pagina Principal
@app.route('/')
def inicio():
    return render_template("principal.html")


# Página potencia:
@app.route('/potencia/<int:base>/<exp>',methods=["GET","POST"])
def potencia(base,exp):
    exp=int(exp)
#Si el exponente es positivo, el resultado es la potencia.
    if exp > 0:
        resultado = base**exp
#Si el exponente es 0, el resultado es 1.
    elif exp==0:
        resultado = 1
#Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.
    elif exp < 0:
        exp = abs(exp)
        resultado = float(1/(base**exp))
    else:
        abort(404)
    return render_template("potencia.html",base=base,exponente=exp,resultado=resultado)


app.run(debug=True)
