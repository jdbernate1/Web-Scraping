
import pandas as pd
import datetime as dt


url='https://www.exchangerates.org.uk/USD-ARS-exchange-rate-history.html'

dolar=pd.read_html(url,header=1)
tabla=dolar[0]
tabla=tabla.drop('Link', axis=1)

nombre_cols = ['Date', 'Cambio']
tabla.columns = nombre_cols

Tasas= tabla["Cambio"].str.split(" ",expand = True) 

tabla['Tasa']=Tasas[3]

tabla=tabla.drop('Cambio', axis=1)

hoy = dt.datetime.today().strftime('%m%Y')  
NombreArchivo = 'CambioUsd_{}.csv'.format(hoy)

tabla.to_csv(NombreArchivo,index=False)