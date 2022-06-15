from Libreria import *;

asientos=generarmatriz(6);
pasajeros=generarmatriz(6);
num=0;
for x in range(6):
    for y in range(6):
        num += 1;
        rellenarmatriz(asientos, x, y, num);
num=0;
for x in range(6):
    for y in range(6):
        num += 1;
        rellenarmatriz(pasajeros, x, y, num);

menu(asientos, pasajeros);
