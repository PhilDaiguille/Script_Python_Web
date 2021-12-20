import os
import os.path
import shutil


def dossier():
    os.mkdir("Projet")
    os.mkdir("Projet/assets")
    os.mkdir("Projet/src")
    os.mkdir("Projet/css")
    os.mkdir("Projet/js")


def file():
    html = open("index.html", "w")
    html.close()
    shutil.move("index.html", "Projet/index.html")
    css = open("style.css", "w")
    css.close()
    shutil.move("style.css", "Projet/css/style.css")
    js = open("app.js", "w")
    js.close()
    shutil.copy("app.js", "Projet/src/app.js")
    shutil.move("app.js", "Projet/js/app.js")


dossier()
file()



