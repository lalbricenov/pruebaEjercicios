"""
This script creates and updates webpages that correspond to exercises.
usage:
    create:
        python pageGenerator.py -c
            materia
            carpeta
    update: 
        python pageGenerator.py -u
            materia
            carpeta
"""

import sys
import os
import io
directory = 'problemSets'

cursos = []
talleres = []


def getIntoFolder(directory, elemsNameSing, elemsNamePlu):
    folderList = os.listdir(directory)
    print(f"{elemsNamePlu.capitalize()}: ")
    for elem in folderList:
        print(f"\t{elem}")
    noExisteElem = True
    elem = ""
    while noExisteElem:
        elem = input(f"Ingrese {elemsNameSing}: ")
        noExisteElem = elem not in folderList
        if noExisteElem:
            print(f"Error: {elemsNameSing} no existe")
    print("\n")
    return elem, os.path.join(directory, elem)


def navigateToTaller():
    materia, materiaPath = getIntoFolder(directory, "materia", "materias")
    curso, cursoPath = getIntoFolder(materiaPath, "curso", "cursos")
    taller, tallerPath = getIntoFolder(cursoPath, "taller", "talleres")
    return {"materia": materia, "curso": curso, "taller": taller, "path": tallerPath}


taller = navigateToTaller()


def htmlEjercicio(num):
    html = f"""<li>
          <h3>Ejercicio {num}</h3>
          <img src="images/{num}.JPG" alt="Ejercicio {num}" />
          <button class="btn btn-secondary butSol" id="butSol{num}">
            Ver solución
          </button>
          <img
            src="images/{num}Sol.JPG"
            class="imgSol"
            id="sol{num}"
            alt="Solucion ejercicio {num}"
          />
        </li>"""
    return html


tema = input("Ingrese el nombre del nuevo taller: ")

headHtml = f""""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{tema}</title>"""
styleHtml = """
    <style>
      body {
        display: grid;
        /* max-width: 800px; */
        justify-items: center;
        justify-self: center;
        grid-template-columns: 1fr minmax(400px, 800px) 1fr;
        grid-template-areas:
          ". ejercicios ."
          ". encuesta .";
      }
      .imgSol {
        display: none;
      }
      img {
        width: 100%;
      }
      #ejercicios {
        grid-area: ejercicios;
      }
      #encuesta {
        grid-area: encuesta;
      }
    </style>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div id="ejercicios">"""
htmlTema = f"<h1>{tema}</h1>"

codigo = input("Ingrese el codigo del nuevo taller: ")
htmlCode = f"""<h3 id="codigo">{codigo}</h3>"""

htmlRecordatorio = """     <p>
          Al terminar de trabajar en los ejercicios debe llenar la encuesta, es de
          caracter obligatorio.
        </p>
        <!-- <h2>Ejercicios</h2> -->
        <ul>
        """


htmlEncuesta = u"""
        </ul>
      </div>
      <div id="encuesta">
        <h2>Autoevaluación</h2>
        <iframe
          width="640"
          height="1050"
          frameborder="0"
          marginheight="0"
          marginwidth="0"
          id="forma"
          >Cargando...</iframe
        >
      </div>
      <script src="writeCode.js"></script>
      <script src="hideAndShow.js"></script>
    </body>
  </html>
  """

fullHtml = headHtml + styleHtml + htmlTema + htmlCode + htmlRecordatorio
images = os.listdir(os.path.join(taller["path"], "images"))
for i in range(0, int(len(images)/2)):
    fullHtml += htmlEjercicio(i+1)
fullHtml += htmlEncuesta

with io.open(os.path.join(taller["path"], 'myFile.html'), 'w', encoding='utf8') as f:
    f.write(fullHtml)
