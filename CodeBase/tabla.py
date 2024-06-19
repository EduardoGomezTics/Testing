# funcion para generar la tabla

def olapilin(clase,fa_sorted,frecuencia_rel, frecuencia_rel_acum):
        
    print('clases','     ','Fa', '              ','Fr', '              ','F acumulada', '     ')
    print('------','     ','-----------','     ','-----------','     ','-----------')
    
    hola = len(clase)
    
    for hola in range(len(clase)):
        print('Clase', clase[hola], '     ',  fa_sorted[hola], '              ', frecuencia_rel[hola], '   ', frecuencia_rel_acum[hola])        