[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2851967&assignment_repo_type=AssignmentRepo)
# practica-semanal-1
Primera práctica semanal del prope-2020

En esta primera práctica utilizaremos github para que empiecen a sentirse cómodas y cómodos con esta plataforma. Esto lo lograremos vía [repl.it](https://repl.it/) y git o github para algunos ejercicios que les pido realicen en Python con repl.it y jupyterlab.

**Ejercicios:**

Realizar ejercicios propuestos por su cuenta de acuerdo a: 

* [Core python](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/1_introduccion/2_core_python.ipynb)

* [Numpy y matplotlib](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/1_introduccion/4_modulos_numpy_matplotlib.ipynb)

La entrega de los ejercicios **es individual** y deben realizarlos en su repo que se creó debajo de la organización de prope-2020-gh-classroom en el momento que uds dieron click a la liga que está en google classroom. La entrega la realizan vía repl.it y git o github y es para el **domingo 14 de junio 11:59 pm**. Deben apoyarse de jupyterlab para que tengan un mejor desarrollo de sus ejercicios. 

Para jupyterlab pueden usar el siguiente botón de binder 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/palmoreck/dockerfiles-for-binder/jupyterlab_prope_r_kernel_tidyerse?urlpath=lab/tree/Propedeutico)

si no tienen instalado jupyterlab de forma local. Recuerden que si le dan click al botón de binder deben descargar los notebooks para que no se pierdan. Otra opción para evitar esto es que utilicen comandos de git:

Si dieron click al botón de binder lo siguiente es posicionarse en el directorio de home (que en el siguiente screenshot es en donde sale la ruta `/home/jovyan`)


<img src="https://dl.dropboxusercontent.com/s/usha3k6p2zf3qt8/%3Ahome%3Ajovyan.png?dl=0" heigth="300" width="300">

Posteriormente deben abrir una terminal (utilizando el símbolo `+` arribita del directorio del screenshot pasado):

<img src="https://dl.dropboxusercontent.com/s/l8y8698lrqow4rw/terminal_jupyterlab.png?dl=0" heigth="300" width="300">

Al abrir la terminal tecleen: bash

<img src="https://dl.dropboxusercontent.com/s/iavm70e1vmi8b6f/home_jupyterlab.png?dl=0" heigth="300" width="300">

Ejecutar lo siguiente:

```
git clone <url de mi repo que está en gh-classroom> <aquí colocar nombre de un directorio>

#el comando anterior les pedirá sus credenciales de github tecleen la respuesta y den enter por cada respuesta

cd <nombre del directorio elegido en la línea anterior> #cd es "change directory" y lo usamos para entrar al directorio

```

Crear un notebook dentro del directorio elegido (con el símbolo `+` abren el menú para crear notebooks) y comiencen a trabajar. Luego en la terminal (asegurándose que están dentro del directorio que tiene su notebook):

```
git config --global user.email "<mi correo asociado de github>"
git config --global user.name "<mi nombre>"
git add <nombre de mi notebook>
git commit -m "mensaje de mi commit" -i <nombre de mi notebook>
git push origin master
```

La última línea les pedirá sus credenciales de github.

Después de realizar por primera vez lo anterior si quiero hacer cambios en mi notebook el flujo que sigo es:

```
#clonar repo a un directorio si no lo tengo clonado
#entrar al directorio con cd
#git config --global user.email "<mi correo asociado de github>"
#git config --global user.name "<mi nombre>"
git commit -m "mensaje de mi commit con los cambios" -i <nombre de mi notebook>
git push origin master
```

La última línea les pedirá sus credenciales de github.


Si decideron no usar git y prefieren usar github para subir los notebooks (que previamente descargué de binder) pueden usar el botón de `Upload files`:

<img src="https://dl.dropboxusercontent.com/s/dvehbsysah6crr3/upload_files_github.png?dl=0" heigth="500" width="500">

y no olviden escribir un mensaje significativo de los cambios que han hecho (incluso si subieron un archivo)


<img src="https://dl.dropboxusercontent.com/s/hk4yp2ncs97hv70/commit_changes.png?dl=0" heigth="500" width="500">

