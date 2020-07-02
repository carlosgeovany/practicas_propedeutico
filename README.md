[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2877759&assignment_repo_type=AssignmentRepo)
# practica-semanal-3-2020
Tercera práctica semanal del prope-2020 

La entrega es para el domingo **28 de junio 11:59 pm**.

Resolver ejercicios que dicen **Tarea** de:


[1_ecuaciones_lineales](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/1_ecuaciones_lineales.ipynb)

[2_interpolacion](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/2_interpolacion.ipynb)

[3_minimos_cuadrados](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/3_minimos_cuadrados.ipynb)

[4_SVD_y_reconstruccion_de_imagenes](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/4_SVD_y_reconstruccion_de_imagenes.ipynb)


Los ejercicios de [1_ecuaciones_lineales](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/1_ecuaciones_lineales.ipynb) y [3_minimos_cuadrados](https://github.com/ITAM-DS/Propedeutico/blob/master/Python/clases/3_algebra_lineal/3_minimos_cuadrados.ipynb) se auto calificarán con github Actions, ver [actions](https://github.com/features/actions) para info sobre este feature de github. Para que funcione esto primero deben revisar que en la tab de Actions:

<img src="https://dl.dropboxusercontent.com/s/kb7ctrv8alqgrs5/actions_gh.png?dl=0" heigth="800" width="800">

tienen activo el "Github Actions Workflow":

<img src="https://dl.dropboxusercontent.com/s/l5bea3adsjyn0yk/actions_gh_2.png?dl=0" heigth="800" width="800">


Si no lo tienen activo avisar al prof. Si lo tienen activo trabajen como normalmente lo realizan subiendo archivos a github.

Se pasa el test si tienen todos los módulos pedidos en la Tarea de las notas. Por cada *commit* realizado se realiza un chequeo que uds pueden revisar en la tab de *Actions*. Por ejemplo:

<img src="https://dl.dropboxusercontent.com/s/oad7cz1cflkuwws/actions_gh_3.png?dl=0" heigth="800" width="800">

<img src="https://dl.dropboxusercontent.com/s/e52qpn0yak01j3l/actions_gh_4.png?dl=0" heigth="800" width="800">



Aquí el botón de *binder* que ayuda para quienes no tienen instalado de forma local jupyterlab:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/palmoreck/dockerfiles-for-binder/jupyterlab_prope_r_kernel_tidyerse?urlpath=lab/tree/Propedeutico)

**Recuerden:**

* Ir guardando su trabajo si usan *binder*.

* Usar git o github para añadir archivos a sus repos de gh-classroom. Algunos comandos de git útiles para añadir un archivo (por ejemplo un notebook) son:

```
git clone <url de mi repo que está en gh-classroom> <aquí colocar nombre de un directorio>

#el comando anterior les pedirá sus credenciales de github tecleen la respuesta y den enter por cada respuesta

cd <nombre del directorio elegido en la línea anterior> #cd es "change directory" y lo usamos para entrar al directorio

```

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

