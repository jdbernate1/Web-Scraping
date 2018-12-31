

import requests 
import time
import pandas as pd
import json

params = {
    'api_key': 't_7qXEU3P2jH',
  }
if __name__=='__main__':
	url='https://www.parsehub.com/api/v2/projects/t7QhCyrVH3yQ/last_ready_run/data'
	response = requests.get(url,params=params)

	#print (response.content)

	if response.status_code==200:
		response_json= response.json() 
		#print (response_json)

tabla = pd.DataFrame.from_records(response_json['selection1'])		

		
dia = time.strftime("%Y%m%d")
ruta='C:/Users/Juan Diego Bernate V/Cookdata Dropbox/Cookdata Dropbox/Origen Datos Reportes BI/9.CAMBIO USD/Dolar Futuro/'
nombre= ruta+ 'dolar_fut_rofex_'+dia+'.csv'

tabla.to_csv(nombre)

"""

def writeToJSONFile(path, fileName, data):
    filePathNameWExt =  path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
    	json.dump(data, fp)

 writeToJSONFile(ruta,nombre,response_json)
 """