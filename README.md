# Papermill Ejemplo 1

<img src="https://th.bing.com/th/id/R.6920b7a1d49c34ccb3ed8e8c66fa89d5?rik=IsdEqlRjKLbOVQ&pid=ImgRaw&r=0" width="500">

[![Python](https://img.shields.io/badge/python-3.11.2-blue)](https://www.python.org/)
[![Papermill](https://img.shields.io/badge/papermill-2.4.0-green)](https://papermill.readthedocs.io/en/latest/)
[![Pandas](https://img.shields.io/badge/pandas-1.5.3-yellow)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.2-orange)](https://scikit-learn.org/)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12-red)](https://seaborn.pydata.org/)

## Índice

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)

## Descripción

Este proyecto es un ejemplo de cómo usar papermill como data pipeline para un caso de un proyecto de machine learning. Papermill es una herramienta que permite ejecutar y parametrizar notebooks de Jupyter. El proyecto consta de cuatro notebooks:

- validacion_datos.ipynb: donde se hace una validación de los datos de entrada y se detectan posibles anomalías o valores faltantes.
- preprocesamiento.ipynb: donde se hace un preprocesamiento de los datos, como normalización, codificación, selección de características, etc.
- modelo.ipynb: donde se entrena un modelo de machine learning usando scikit-learn y se evalúa su rendimiento.
- prediccion.ipynb: donde se hace una predicción sobre nuevos datos usando el modelo entrenado y se muestra el resultado.

Este ejemplo es un submódulo de otro git que contiene todos los ejemplos desarrollados.

## Instalación

Para ejecutar este proyecto se necesita tener instalado Python 3.6 o superior y las siguientes librerías:

- papermill 2.X o superior
- pandas 1.X
- numpy 1.X
- scikit-learn 1.X
- seaborn 0.12 o superior

Se recomienda usar un ambiente virtual para instalar las librerías y evitar conflictos con otras versiones. Se puede crear un ambiente virtual **(para Windows)** usando los comandos:

Crea un ambiente virtual llamado venv
```bash
python -m venv venv
```
Activa el ambiente virtual
```bash
venv/scripts/activate
```
Instala las librerías y las actualiza si es necesario
```bash
pip install -r requirements.txt --upgrade
```

En caso de usar Linux o Mac, los comandos cambian un poco su sintaxis. Se recomenda revisar como crear ambientes virtuales en dichos OS si se desea ejecutar el código en alguna distribución de Linux o Mac.

Para instalar el proyecto desde el repositorio que lo contiene como submódulo, se puede usar el comando git clone con la opción --recurse-submodules. Por ejemplo, se podría usar este comando:

```bash
git clone --recurse-submodules https://github.com/LeandroNardiTaligent/Papermill-Ejemplos
```

## Uso

Para usar este proyecto, se deben seguir los siguientes pasos:

1. Ejecutar el archivo `datos_simulados.py`. Este archivo genera un conjunto de datos sintéticos llamado `dataset.xlsx` para el problema de regresión lineal y lo guarda en la carpeta `input/`. Si la carpeta `input/` no existe, el archivo la creará automáticamente.
2. Ejecutar el script `main.bat`. Este script se encarga de llamar a los otros notebooks con los parámetros adecuados mediante papermill. Los resultados de cada notebook ejecutadas por el script se guardan en archivos con el sufijo _output.ipynb en la misma carpeta donde se encuentran las notebooks.
3. Finalizada la ejecución de `main.bat`, se crea el archivo `predicciones.xlsx` en la carpeta `output/`. Este archivo contiene las predicciones del modelo de regresión lineal sobre nuevos datos generados artificialmente. Si la carpeta `output/` no existe, el notebook la creará automáticamente.

**Nota**: Si se ejecuta este ejemplo en otro OS, hay que re-escribir el script .bat en el formato que corresponda. Ejemplo, si se quiere correr en una distribución Linux, habrá que crear el archivo `main.sh` y adaptar los comandos del script hecho en Windows para bash

## Contribución

Este proyecto es solo un ejemplo didáctico y no tiene fines comerciales. Si quieres contribuir a mejorar el código o la documentación, puedes hacer un fork del repositorio y enviar un pull request con tus cambios.

<br>

## <center> Made with &#x2764; for Advanced Analitycs</center>

<br>

<center><a href="https://www.taligent.com.ar/es/"><img src="https://www.taligent.com.ar/wp-content/uploads/2022/09/logo-e1664303535353-300x66.png" width='200'></a></center>
