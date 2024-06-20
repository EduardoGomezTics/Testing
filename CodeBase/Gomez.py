import math

def clases_grouped(datos):
    
    
    rango = max(datos)-min(datos)
    
    clases = 1 + 3.3 * math.log(len(datos))
    
    clases_redondear = round(clases)
    
    ancho = rango/clases_redondear
    
    lim_inf = []
    lim_sup = []
    mrks = []
    
    for elementos in clases:
        lim_inf.append()