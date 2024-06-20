def tabla_grouped(clases, lim_inf, lim_sup, mrks):
    print("{:^10}".format("Clase"), "{:^20}".format("Limite Inferior"), "{:^20}".format("Limite Superior"), "{:^15}".format("Marca de clase"))
    print("----------", "-------------------", "-------------------", "---------------")
    
    for i in range(len(clases)):
        print("{:^10}".format(f"Clase {clases[i]}"), "{:^20.3f}".format(lim_inf[i]), "{:^20.3f}".format(lim_sup[i]), "{:^15.3f}".format(mrks[i]))
