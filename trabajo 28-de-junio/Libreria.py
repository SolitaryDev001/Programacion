import os;
os.system("cls");
import numpy as np;
vips=[];
normales=[];

def generarmatriz(num):
    return np.empty((num,num));

def rellenarmatriz(matriz, x, y, num):
    matriz[x,y] = num;

def asientoValid():
    valid = False;
    asiento=0;
    while not valid:
        try:
            asiento=int(input("Inserte Numero de Asiento "));
    
            if (asiento > 0 and asiento < 37):
                valid = True;
                break;
            else:
                valid = False;
                print("Debes Ingresar un Asiento Valido");
        except ValueError:
            print("El Numero debe ser Entero");
    
    return asiento;

def precioAsiento(num):
    precio = 0;

    if (num > 0 and num<13):
        precio=3000000;
        vips.append(1);
    else:
        precio=1500000;
        normales.append(1);

    return precio;

def precioAsientoB(num):
    precio = 0;

    if (num > 0 and num<13):
        precio=3000000;
        vips.remove(1);
    else:
        precio=1500000;
        normales.remove(1);

    return precio;

def rellenarAsiento(matriz, num, rut):
    if (matriz.flat[num-1] == 0):
        print("El CAMAROTE se encuentra OCUPADO");
        return 0;

    matriz.flat[num-1] = 0;
    precio_asiento = precioAsiento(num);
    print("Total a Pagar", precio_asiento);
    return precio_asiento;

def eliminarAsiento(matriz, matrizb, num):
    if (matriz.flat[num-1] != 0):
        print("El CAMAROTE no se encuentra OCUPADO");
        return 0;

    matriz.flat[num-1] = num;
    precio_asiento = precioAsientoB(num);
    print("Pasajero ELIMINADO ", int(matrizb.flat[num-1]));
    quitarPasajero(int(matrizb.flat[num-1]));
    return precio_asiento;

def rellenarPasajero(matriz, num, rut):
    if (matriz.flat[num-1] == 0):
        return;

    matriz.flat[num-1] = rut;
    print("\n\nAgregando rut", agregarPasajero(rut), "Como Pasajero");

def eliminarPasajero(matriz, num):
    if (matriz.flat[num-1] != 0):
        return;

    print("\n\nEliminando Pasajero, " + quitarPasajero(num));
    matriz.flat[num-1] = num;

rut_pasajeros=[];
def agregarPasajero(rut):
    rut_pasajeros.append(rut);
    return rut;

def quitarPasajero(num):
    rut_pasajeros.remove(num);
    return num;

def rutValid():
    while True:
        try:
            rut_pasajero=int(input("Ingresa un RUT "));
            long_rut = len(str(rut_pasajero));
            if (long_rut > 7 and long_rut < 10):
                return rut_pasajero;
            else:
                print("El rut debe tener mas de 8 caracteres, rut sin guion");
        except ValueError:
            print("Debes Ingresar tu Rut sin guion");

def optionValid():
    while True:
        try:
            op=int(input("Ingresa una Opcion "));
            if (op > 0 and op < 7):
                return op;
            else:
                print("Opcion Invalida");
        except ValueError:
            print("Debes Ingresar un Numerico");

def menu(matriz, matrizb):
    total_pagar=0;
    while True:
        print("El bote a remos\n1. Mostrar camarotes disponibles\n2. Comprar Boleto\n3. Totales\n4. Anular venta\n5. Listado de pasajeros\n6. Salir");
        op = optionValid();

        if (op == 1):
            print(matriz);

        if (op == 2):
            asiento = asientoValid();
            rut_pasajero=rutValid();

            rellenarPasajero(matrizb, asiento, rut_pasajero);
            total_pagar += rellenarAsiento(matriz, asiento, rut_pasajero);
        
        if (op == 3):
            print("Cantidad de VIP => ", len(vips));
            print("Cantidad de NORMALES => ", len(normales));
            print("Total a PAGAR => ", total_pagar);

        if (op == 4):
            asiento = asientoValid();

            eliminarPasajero(matrizb, asiento);
            total_pagar -= eliminarAsiento(matriz, matrizb, asiento);

        if (op == 5):
            if (len(rut_pasajeros) == 0):
                print("No hay Pasajeros");
            else:
                print("Lista de Pasajeros");
                pasajeros = sorted(rut_pasajeros, key=int, reverse=False); 
                for pasajero in pasajeros:
                    print(pasajero);
        
        if (op == 6):
            print("Hasta la proxima, turururu");
            os.system("start www.youtube.com/watch?v=b8PxzPxI8Os");
            break;

        os.system("pause");
    return op;
