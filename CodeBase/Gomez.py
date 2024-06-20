import math

def clases_grouped(datos):
    rango = max(datos) - min(datos)
    clases = 1 + 3.3 * (math.log(len(datos))/2)
    clases_redondear = round(clases)-1
    ancho = rango / clases_redondear
    
    lim_inf = [min(datos)]
    lim_sup = []
    mrks = []
    
    for i in range(clases_redondear - 1):
        lim_inf.append(lim_inf[-1] + ancho)
        lim_sup.append(lim_inf[-1] + ancho)
        mrks.append((lim_inf[-1] + lim_sup[-1]) / 2)
    
    lim_sup.append(max(datos))
    mrks.append((lim_sup[-1] + lim_inf[-1]) / 2)
    
    return lim_inf, lim_sup, mrks