# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:53:43 2021

@author: ivanp
"""
import math as mt

# Grados, min, seg a decimal
def dms_to_dd(d, m, s):
    if (d >=0):
        dd = float(d) + float(m)/60 + float(s)/3600
    else:
        dd = float(d) - float(m)/60 - float(s)/3600
    return round(dd,4)


# Decimal a Grados, min, seg
def dd_to_dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    md = round(md,4)
    m = int(md)
    sd = (md - m) * 60
    sd = round(sd,4)
    return [d, m, sd]

# Formula de Coseno
def cos(PZ, ZE, Z):
    rPZ = mt.radians(PZ)
    rZE = mt.radians(ZE)
    rZ = mt.radians(Z)
    cosPE = mt.cos(rPZ)*mt.cos(rZE)+mt.sin(rPZ)*mt.sin(rZE)*mt.cos(rZ)
    return round(cosPE,4)

# Formula de Seno
def sen(ZE, PE, Z):
    rZE = mt.radians(ZE)
    rPE = mt.radians(PE)
    rZ = mt.radians(Z)
    sinP = (mt.sin(rZE)*mt.sin(rZ))/mt.sin(rPE)
    return round(sinP,4)
    
# Coordenadas Horizontales
a = dms_to_dd(153, 31, 2)
h = dms_to_dd(67, 50, 56)
g = dms_to_dd(-40, 50, 30)
tth = dms_to_dd(12, 9, 9)

# Relaciones
PZ = 90 - g
ZE = 90 - h
Z = 180 - a
Z = round(Z,4)

# Usando la formula del coseno
csPE = cos(PZ, ZE, Z)

# Obteniendo el valor de PE
PE = mt.degrees(mt.acos(csPE))
PE = round(PE,4)

# Obteniendo el valor de delta
d = round(90 - PE,4)
d = dd_to_dms(d)

# Usando la formula del Seno
snP = sen(ZE, PE, Z)

# Obteniendo P
P = mt.degrees(mt.asin(snP))
P = round(P,4)

Hr = P

Hrh = dd_to_dms(Hr/15)
Hrd = dms_to_dd(Hrh[0], Hrh[1], Hrh[2])

alph = tth - Hrd
if (alph < 0):
    alph = alph + 24
    
alph = dd_to_dms(alph)

#Resultados
print("La solucion es:")
print("alpha =", alph, "h, m, s")
print("delta =", d, "°, ', ''")