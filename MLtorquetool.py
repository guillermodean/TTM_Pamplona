import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

df=pd.read_csv('Results_TTM.csv',sep=";",header=0)
df=df.drop(columns=["Step status","Current trend","Torque rate min","Torque rate max","Torque rate trend","CVILOGIX","Identifier6","Identifier7","Identifier8","Identifier9","Identifier10","Second transducer torque deviation","Second transducer angle deviation","Result type","Pulse counter","Angle offset","AO torque rate"])
print(df.info())
print(df.describe())
#pivot=pd.pivot_table(df,values="Torque",index="Pset name",columns="Controller name",aggfunc='mean')

#TODO identificar los pares que fallan por angulo de seguridad
oknokresults=df[['Result status','Torque','Angle','Pset name','Controller name']] #TODO quitar filas que contengan pokayokes
nok_results=oknokresults[oknokresults['Result status'].str.contains("NOK")]
nok_results=nok_results.rename(columns={'Pset name':'Pset_name','Controller name':'Controler_name',"Result status":"Result_status"})
"""nok_results_slides=nok_results[nok_results['Pset name'].str.contains("Slide")]
nok_results_slides_BAU=nok_results_slides[nok_results_slides['Controller name'].str.contains("BAU")]
Torque_low_slides=len(nok_results_slides_BAU.loc[nok_results_slides_BAU['Torque']<18])
Torque_high_slides=len(nok_results_slides_BAU.loc[nok_results_slides_BAU['Torque']>24])
title_slides='por abajo: '+str(Torque_low_slides)+' por arriba: '+str(Torque_high_slides)
sns.scatterplot(data=nok_results_slides_BAU, x=nok_results_slides_BAU['Angle'], y=nok_results_slides_BAU['Torque'], hue=nok_results_slides_BAU['Pset name']).set_title(title_slides) #ojo le cuesta"""
#hay 208 psets
nok_results_gby=nok_results.groupby('Pset name').mean()
sns.histplot(data=nok_results_gby['Torque']).set_title('medias')
#fallan muchas por par cero
sns.histplot(data=nok_results_gby['Angle']).set_title('medias')
#fallan muchas por angulo cero
#TODO regex expresion to identify the torque target of each pset (dos numeros, separados por punto, entre espacios o seguidos de Nm)
