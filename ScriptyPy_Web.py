import os
import os.path
import shutil


# Version 1.5 - Fix + Add Readme

def dossier():
    os.mkdir("Projet")
    os.mkdir("Projet/assets")
    os.mkdir("Projet/css")
    os.mkdir("Projet/js")


def css():
    css = open("style.css", "w")
    css.write("/* RESET 2022 */\nhtml{\n\tfont-size:62.5%;\n\tscroll-behavior:smooth;\n}\nbody{"
              "\n\tfont-size:1.6rem;\n\tmargin:0;\n}\nsection,figure,h1,h2,h3,h4,h5,h6,ol,p,"
              "ul{\n\tmargin:0;\n\tpadding:0;\n\tlist-style:none;\n}\na{"
              "\n\tcolor:#000;\n\ttext-decoration:none;\n}\n*{ "
              "\n\tbox-sizing:border-box;\n}\nbutton{"
              "\n\tpadding:0;\n\tborder:0;\n\tbackground-color:transparent;\n} "
              "\nimg{\n\tdisplay: inline-block;\n\twidth: 100%;\n\theight: 100%;\n\tobject-fit: cover;\n}\n/*"
              "HEADER */\n\n\n\n/* MAIN */\n\n\n\n/* FOOTER */\n\n\n\n/* @Copyright - PhilDaiguille*/")  # reset
    css.close()
    shutil.move("style.css", "Projet/css/style.css")


def file():
    html = open("index.html", "w")
    html.write('<!DOCTYPE html>\n<html lang="fr">\n<head>\n\t<meta charset="UTF-8">\n\t<meta '
               'http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, '
               'initial-scale=1.0">\n\t<title>Document</title>\n\t<link rel="stylesheet" '
               'href="./css/style.css">\n</head>\n\n<body>\n<header>\n<h1>Projet</h1>\n</header>\n<main>\n</main>\n'
               '<footer>\n\t<p '
               '>&copy; - 2022 -  </p>\n</footer>\n<script src="./js/app.js"></script>\n</body>\n\n</html>')
    html.close()
    shutil.move("index.html", "Projet/index.html")

    gitignore = open(".gitignore", "w")
    gitignore.close()
    shutil.move(".gitignore", "Projet/.gitignore")

    readme = open("readme.md", "w")
    readme.write("# Projet WEB \n\n## Description :\n\n## [Voir le lien]()\n\n## Utilisation :\n\n")
    readme.close()
    shutil.move("readme.md", "Projet/readme.md")

    css()

    js = open("app.js", "w")
    js.write('document.addEventListener("DOMContentLoaded", () => {\n\t/*APP*/\n\tconsole.log("charged")\n});')
    js.close()
    shutil.move("app.js", "Projet/js/app.js")


dossier()
file()
