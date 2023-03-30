import os
import json
import pandas as pd

PATH = os.getcwd()
AUX_FOLDER = 'aux_file'
FILENAME = 'scaler.xlsx'

df_scaler = pd.read_excel(os.path.join(PATH, AUX_FOLDER, FILENAME))
media = df_scaler.Media.to_list()
std = df_scaler.STD.to_list()

with open(os.path.join(PATH, AUX_FOLDER, 'params.json'), 'w') as f:
    json.dump({'media': media, 'desv_estandar': std}, f)
