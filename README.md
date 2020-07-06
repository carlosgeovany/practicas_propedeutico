[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2890793&assignment_repo_type=AssignmentRepo)
# practica-semanal-4-2020
 Cuarta práctica semanal del prope-2020 


**1) Leer, ejecutar y proponer sus propios ejemplos en computadora de uso del lenguaje R de:**

* [Propedeutico/R/clases/1_introduccion/2_core_R.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/1_introduccion/2_core_R.ipynb)

* [Propedeutico/R/clases/1_introduccion/3_ggplot2.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/1_introduccion/3_ggplot2.ipynb)

**para este primer punto les recomiendo usar jupyter *notebooks* y nombrarlos como las notas o con un nombre que sea fácil identificarlos de los archivos que suben o dentro de directorios, uds deciden**.

**2) Realizar los ejercicios de las siguientes notas en papel excepto en los ejercicios que explícitamente se mencione se hagan en computadora. La entrega la realizan con una liga en el `README.md` de la raíz de su repo de gh-classroom que dirija a un servicio externo de almacenamiento (por ejemplo google drive, dropbox,...) con los ejercicios realizados. Otra opción es realizar los ejercicios en *notebooks* de jupyterlab y subirlos a su repo de gh-classroom (así escribirían con *Markdown*, *Latex* y lenguaje de R)**.

* [Propedeutico/R/clases/2_probabilidad/1_elementos_de_probabilidad.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/1_elementos_de_probabilidad.ipynb)

* [Propedeutico/R/clases/2_probabilidad/2_propiedades_de_la_probabilidad.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/2_propiedades_de_la_probabilidad.ipynb)

* [Propedeutico/R/clases/2_probabilidad/3_metodos_de_conteo.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/3_metodos_de_conteo.ipynb)

* [Propedeutico/R/clases/2_probabilidad/4_probabilidad_condicional.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/4_probabilidad_condicional.ipynb)

* [Propedeutico/R/clases/2_probabilidad/5_independencia.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/5_independencia.ipynb)

* [Propedeutico/R/clases/2_probabilidad/6_teorema_de_Bayes.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/6_teorema_de_Bayes.ipynb)

* [Propedeutico/R/clases/2_probabilidad/7_variables_aleatorias.ipynb](https://github.com/ITAM-DS/Propedeutico/blob/master/R/clases/2_probabilidad/7_variables_aleatorias.ipynb)


**Notas:**

**1) No suban archivos con extensión `html` o `Rmd` pues al darle click en éstos no es posible visualizarlos en github (esto lo escribo por si generan archivos con Rstudio)**

**2) Aquí el botón de binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/palmoreck/dockerfiles-for-binder/jupyterlab_prope_r_kernel_tidyerse?urlpath=lab/tree/Propedeutico) (también permite uso de R, sólo hay que asegurarse que el kernel es el de R)**

<img src="https://dl.dropboxusercontent.com/s/o8e6xk5xwhlzzgj/r_kernel_jupyterlab.png?dl=0" heigth="800" width="800">

<img src="https://dl.dropboxusercontent.com/s/82kjtun9r2lv28t/r_kernel_jupyterlab_2.png?dl=0" heigth="300" width="300">

**3) Si usan repl y quieren utilizar el botón de *run* de repl coloquen en el archivo `.replit` `language = "rlang"` y para el `run = ""` escriban el script que quieran ejecutar vía un `Rscript` o `R CMD BATCH`, por ejemplo:**

<img src="https://dl.dropboxusercontent.com/s/z0jf8hre4qci6yb/repl_for_r_kernel.png?dl=0" heigth="600" width="600">

**(el uso de `Rscript` o `R CMD BATCH` funciona desde la consola o línea de comandos)**.

**4) Si usan repl y quieren instalar librerías de R allí pueden utilizar lo siguiente:**

```
# Example:

.libPaths(new='~/R/')
dir.create('~/R', showWarnings = FALSE, recursive = TRUE)
.libPaths()
install.packages("<aquí colocar el nombre del paquete>")
```

**Para instalar paquetes en jupyter notebooks se puede utilizar en una celda:**

```
install.packages("<aquí colocar el nombre del paquete>",lib="/usr/local/lib/R/site-library/",
                repos="https://cran.itam.mx/",verbose=TRUE)
```

**Recuerden:**

* Ir guardando su trabajo si usan *binder*.

* Usar git o github para añadir/modificar archivos a sus repos de gh-classroom de forma continua. Algunos comandos de git útiles para añadir un archivo (por ejemplo un notebook) son:

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

Después de realizar por primera vez lo anterior (añadir un archivo) si quiero hacer cambios en mi notebook el flujo que sigo es:

```
#clonar repo a un directorio si no lo tengo clonado
#entrar al directorio con cd
#git config --global user.email "<mi correo asociado de github>"
#git config --global user.name "<mi nombre>"
git commit -m "mensaje de mi commit con los cambios" -i <nombre de mi notebook>
git push origin master
```

La última línea les pedirá sus credenciales de github.
