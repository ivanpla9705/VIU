
"""
Created on Wed Dec  1 18:32:06 2021

@author: ivanp
"""
#Librerias Necesarias
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Constantes
Ms = 9e29#kg
Msl = 0.45#masas solares
Rs = 320.16e6#m
Ts = 3350#Kelvin
Pa = 7.21e-3#años sidereos
P = 2.6439#dias
Psg = 228432.96#segundos
G = 6.674e-11#constante gravitacional
e = 0.16#exentricidad

#  Lectura de los datos
df= pd.read_table('TRANSITO.txt', 
                  delim_whitespace=True)
data = pd.read_table('RV_HIRES.txt', 
                     delim_whitespace=True)

#  Renombrando columnas
df.columns = ["HJD", "Flux", "Noise"]
data.columns = ["Time", "Velocity", "Error", "Phase"]
data["Time"] = data["Time"].apply(lambda x: x/365)


#  Convirtiendo a numpy.array
xdata = np.array(df["HJD"])
ydata = np.array(df["Flux"])


#  Plot de los datos
plt.xlabel("HJD")
plt.ylabel("Flux")
plt.title('Flux variation over time')
plt.plot(xdata, 
         ydata,
         "o", 
         color="blue",
         linestyle=":", 
         label="Flux" )

plt.grid(ls="--",
         color="#000000",
         alpha=0.7)

plt.legend(frameon=False,
           ncol=2,
           loc="lower left",
           fontsize=14)

plt.tight_layout()
plt.savefig("graf_FV.png")
plt.show()

#Funcion del fit
def cos_func(x, a, b, c):
    return a*np.cos(b*x+c)

#  Convirtiendo a numpy.array
xdata = np.array(data["Phase"])
ydata = np.array(data["Velocity"])
yerr = np.array(data["Error"])

# Curva del fit
parameters, covariance = curve_fit(cos_func,
                                   xdata,
                                   ydata)
# Parametros
fit_D = parameters[0]
fit_E = parameters[1]
fit_F = parameters[2]

# Creando fit en x
x_fit = np.linspace(0, 1, 100)

# Creado fit en y
fit_cos = cos_func(x_fit,
                   fit_D,
                   fit_E,
                   fit_F)
#  Plot de los datos
plt.errorbar(xdata,
             ydata,
             yerr=yerr,
             fmt=".k",
             ecolor="#3f37c9",
             label="Data")
plt.xlabel("Phases")
plt.ylabel("radial velocity [m/s]")
plt.title('Radial velocity')
plt.plot(x_fit,
         fit_cos,
         label='Fit',
         ls="--",
         color="#b5179e")
plt.xlim(0, 1)
plt.xticks(np.linspace(0, 1, 11))
plt.ylim(-35, 35)
plt.yticks(np.linspace(-35, 35, 11))
plt.grid(ls="--",
         color="#000000",
         alpha=0.7)
plt.legend(frameon=False,
           ncol=2,
           loc="upper left",
           fontsize=14)
plt.tight_layout()
plt.savefig("graf_RV.png")
plt.show()

#-----------------------Resultados------------------
#Diferencia de flujo/Profundidad de Transito
c1=max(df["Flux"])  
c2=min(df["Flux"])
TD=(c1-c2)/c1

#Radio del planeta
Rp = (np.sqrt(TD))*(Rs)

#Distancia Estrella - Planeta 
a = np.cbrt(Msl*(Pa**2))#UA
a2 = a*149597870.7#km

#Semi-amplitud
k = max(fit_cos) #basado en el fit
k2 = max(ydata) #basado en los datos

#Calculo de masa minima y real
Mmin = (4.92e-3)*(np.sqrt(1-(e**2)))*k*(np.cbrt(P))*(Msl**(2/3))#Masa minima del planeta
Mp = (Ms*k*Psg)/(2*np.pi*(a2*1000))#Masa real
Mpj = Mp/(1.898e27)#Masa en masas de Jupiter
Mpt = Mp/(5.97e24)#Masa en masas terrestres
Mps = Mp/(2e30)#Masa en masas solares

#Calculo de densidad
d = (3*Mp)/(4*np.pi*((Rp)**3))#kg/m^3
dg = d*1000/(100**3)#g/cm^3

#Calculo de la temp. de equilibrio
Teq = Ts*(np.sqrt((Rs/1000)/(2*a2)))#albedo 0
Teqa = Ts*((1-0.3)**(1/4))*(np.sqrt((Rs/1000)/(2*a2)))#albedo de la tierra = 0.3

#Print de resultados
print("La profundidad de transito es",round(TD,4)) 
print()
print("El radio del Planeta es", round(Rp,2),"m","o", round(Rp/1000,2),"km")
print()
print("La distancia estrella-planeta es",round(a,2),"UA")
print( "que es igual a",round(a2,2),"km" )
print()
print("El valor de k basado en el fit es:", round(k,2),"m/s")
print("El valor de k basado en los datos es:", k2,"m/s")
print()
print("La masa minima del planeta es", round(Mmin,2),"masas de Jupiter")
print()
print("La masa real del planeta es de", round(Mp,2), "kg")
print("lo que es igual a",round(Mpj,2),"masas de Jupiter")
print("o",round(Mpt,2),"masas terrestres","o",round(Mps,4),"masas solares")
print()
print("La densidad del planeta es",round(d,2),"kg/m^3", "o",round(dg,2),"g/cm^3")
print()
print("La temperatura de equilibrio con un albedo nulo, es",round(Teq,2),"K")
print("con el albedo medio de la Tierra (0.3), es",round(Teqa,2),"K")
