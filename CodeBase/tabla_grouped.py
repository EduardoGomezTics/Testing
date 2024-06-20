def tabla_grouped(clase, lim_inf, lim_sup, mrks):
    print('Clase', '   ', 'Lim Inf', '   ', 'Lim Sup', '   ', 'Marca')
    print('------', '   ', '---------', '   ', '---------', '   ', '-----')
    
    for i in range(len(clase)):
        print('Clase', clase[i], ' ', round(lim_inf[i], 3), '   ', round(lim_sup[i], 3), '   ', round(mrks[i], 3))

