# Development


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Data-set1.csv')



AB = df[df['Province'] == 'AB']
MB = df[df['Province'] == 'MB']
PEI = df[df['Province'] == 'PEI']
NB = df[df['Province'] == 'NB']
ON = df[df['Province'] == 'ON']
SK = df[df['Province'] == 'SK']
NL = df[df['Province'] == 'NL']
QC = df[df['Province'] == 'QC']
BC = df[df['Province'] == 'BC']
NS = df[df['Province'] == 'NS']

plt.plot(AB['Year'],AB['NX Interprovincial Services'])
plt.plot(MB['Year'],MB['NX Interprovincial Services'])
plt.plot(PEI['Year'],PEI['NX Interprovincial Services'])
plt.plot(NB['Year'],NB['NX Interprovincial Services'])
plt.plot(ON['Year'],ON['NX Interprovincial Services'])
plt.plot(SK['Year'],SK['NX Interprovincial Services'])
plt.plot(NL['Year'],NL['NX Interprovincial Services'])
plt.plot(QC['Year'],QC['NX Interprovincial Services'])
plt.plot(BC['Year'],BC['NX Interprovincial Services'])
plt.plot(NS['Year'],NS['NX Interprovincial Services'])
plt.grid(True)
plt.legend(['Alberta','Manitoba','Prince Edward','New Brunswick','Ontario','Saskachuwan','New Foundland','Qubec','Britch Colm','Nova Scotia'])
plt.show()
