from flask import Flask, render_template, request, redirect, url_for
import datetime


app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template("index.html")

@app.route("/age")
def age():
    a=2022-2002
    return render_template("age.html", agee=a)

liste_étudiant =[
    { 'nom' : 'Bouyemmout' , 'prénom' : 'meriem' , 'classe' : 'G1'  },
    { 'nom' : 'Souci' , 'prénom' : 'Nour' , 'classe' : 'G2'  },
    { 'nom' : 'Sfendji' , 'prénom' : 'Lina' , 'classe' : 'G1'  },
    { 'nom' : 'Mahdi' , 'prénom' : 'Maya' , 'classe' : 'G1'  }
]
@app.route("/étudiant")
def étudiant():
    clé=request.args.get('c')
    if clé:
        eleves_selectionnes = [eleve for eleve in liste_étudiant if eleve['classe'] == clé]
    else:
        eleves_selectionnes = []
    return render_template("étudiant.html", e=eleves_selectionnes)
    
@app.route("/inscrire")
def inscrire():
    return render_template("inscrire.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        if nom == 'meriem' and mdp == '2020':
            return render_template("traitement.html", nom_utilisateur=nom)
        else:
            return render_template("traitement.html")
    else:
        return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug=True)



