# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:21:53 2021

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

# Coseno de HOc
def tan(d,g):
    dr = mt.radians(d)
    gr = mt.radians(g)
    csHoc = -mt.tan(dr)*mt.tan(gr)
    return round(csHoc,4)

# Sen z
def sen(POc, HOc, ZOc):
    rPOc = mt.radians(POc)
    rHOc = mt.radians(HOc)
    rZOc = mt.radians(ZOc)
    SnZ = (mt.sin(rPOc)*mt.sin(rHOc))/mt.sin(rZOc)
    return round(SnZ,4)

d = dms_to_dd(7, 26, 2)
g = dms_to_dd(39, 28, 30)
alph = dms_to_dd(3, 28, 50)

#Verificamos la condicion
if (abs(d) > (90 - abs(g))):
    exit()

PZ = 90 - g
ZOc = 90 
POc = 90 - d

CosHoc = tan(d,g)

Hoc = mt.degrees(mt.acos(CosHoc))
Hoc = round(Hoc,4)

Toc = alph + (Hoc/15)
Tor = alph - (Hoc/15)
if (Tor < 0):
    Tor = Tor +24

Toc = dd_to_dms(Toc)
Tor = dd_to_dms(Tor)

SenZ = sen(POc, Hoc, ZOc)
Z = mt.degrees(mt.asin(SenZ))
Z = round(Z,4)

aoc = 180 - Z
aor = 360 - aoc

print("Hora siderea del ocaso:", Toc, "h, m, s")
print("Hora siderea del orto:", Tor, "h, m, s")
print("")
print("coordenadas ocaso:", dd_to_dms(aoc),"°, ', ''")
print("coordenadas orto:", dd_to_dms(aor), "°, ', ''")