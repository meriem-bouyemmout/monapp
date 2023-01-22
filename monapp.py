from flask import Flask, render_template, request, redirect, url_for
import datetime
import sqlite3 




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

@app.route("/traitement1", methods=["POST", "GET"])    
def traitement1():
    if request.method == "POST":
       d = request.form
       no1 = d.get('nom1')
       pr1 = d.get('prénom1')
       md1 = d.get('mdp1')
       de =[(no1, pr1, md1)]
       conn = sqlite3.connect('inscription.db')
       cur = conn.cursor()
       for i in de:
        req="insert into client (nom, prénom, mot_de_passe) values (?, ?, ?) "
        cur.execute(req, i)
        conn.commit()
        conn.close()
    return "inscription valider"




@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if  request.method == "POST":
        donnees = request.form
        no = donnees.get('nom')
        md = donnees.get('mdp')
        te  = [(no)]
        te1 = [(md)]
        conn = sqlite3.connect('inscription.db')
        cur = conn.cursor()
        
        
        req  = "select nom from client where nom = '{no}' and mot_de_passe ='{md}'  "                       
        cur.execute(req)       
        res = cur.fetchall()

        if res is True : 
           return "le nom d'utilisateur ou le mot de passe invalider "
        else : 
           return "Bienvenue '{no}' "
       
       



if __name__ == '__main__':
    app.run(debug=True)