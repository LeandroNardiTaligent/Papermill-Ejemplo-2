cd %~dp0

call venv\scripts\activate.bat

papermill validacion_datos.ipynb validacion_datos_output.ipynb

papermill preprocesamiento.ipynb preprocesamiento_output.ipynb

papermill modelo.ipynb modelo_output.ipynb

python get_params.py

papermill prediccion.ipynb prediccion_output.ipynb -f aux_file/params.json

pause