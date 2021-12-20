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
    css = css.write("/* RESET 2022 */\nhtml{\n\tfont-size:62.5%;\n\tscroll-behavior:smooth;\n}\nbody{"
                    "\n\tfont-size:1.6rem;\n\tmargin:0\n}\nsection,figure,h1,h2,h3,h4,h5,h6,ol,p,"
                    "ul{\n\tmargin:0;\n\tpadding:0;\n\tlist-style:none;\n}\na{"
                    "\n\tcolor:#000;\n\ttext-decoration:none;\n}\n*{ "
                    "\n\tbox-sizing:border-box;\n}\nbutton{"
                    "\n\tpadding:0;\n\tborder:0;\n\tbackground-color:transparent;\n}\n/* "
                    "HEADER */")  # reset
    shutil.move("style.css", "Projet/css/style.css")
    css.close()

    js = open("app.js", "w")
    js.close()
    shutil.copy("app.js", "Projet/src/app.js")
    shutil.move("app.js", "Projet/js/app.js")


dossier()
file()
