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
        precio=3500000;
        vips.append(1);
    else:
        precio=1500000;
        normales.append(1);

    return precio;

def precioAsientoB(num):
    precio = 0;

    if (num > 0 and num<13):
        precio=3500000;
        vips.remove(1);
    else:
        precio=1500000;
        normales.remove(1);

    return precio;

def rellenarAsiento(matriz, num, rut):
    if (matriz.flat[num-1] == 0):
        print("El Camarote ya se encuentra Asignado", "\n***********************************");
        return 0;

    matriz.flat[num-1] = 0;
    precio_asiento = precioAsiento(num);
    print("Precio del asiento: ", precio_asiento, "\n***********************************");
    return precio_asiento;

def eliminarAsiento(matriz, matrizb, num):
    if (matriz.flat[num-1] != 0):
        print("El Camarote no se encuentra Asignado", "\n***********************************");
        return 0;

    matriz.flat[num-1] = num;
    precio_asiento = precioAsientoB(num);
    print("Pasaje de Asiento", num, "Eliminado", "\n***********************************");
    quitarPasajero(int(matrizb.flat[num-1]));
    return precio_asiento;

def rellenarPasajero(matriz, num, rut):
    if (matriz.flat[num-1] == 0):
        return;

    matriz.flat[num-1] = rut;
    titulo();
    print("RUN", agregarPasajero(rut), "Asignado al asiento", num);

def eliminarPasajero(matriz, num):
    if (matriz.flat[num-1] != 0):
        return;

    print("El Asiento", num, "Fue Reembolsado", "\n***********************************");
    matriz.flat[num-1] = num;

def mostrarMatriz(matriz):
    for x in range(5):
        print("|\t", int(matriz[x,0]),"\t",int(matriz[x,1]),"\t",int(matriz[x,2]),"\t",int(matriz[x,3]),"\t",int(matriz[x,4]),"\t",int(matriz[x,5]), "\t|");

    for x in range(2):
        print("|___________________________    ________________________|");
    
    print("|\t", int(matriz[5,0]),"\t",int(matriz[5,1]),"\t",int(matriz[5,2]),"\t",int(matriz[5,3]),"\t",int(matriz[5,4]),"\t",int(matriz[5,5]), "\t|");

rut_pasajeros=[];
def agregarPasajero(rut):
    rut_pasajeros.append(rut);
    return rut;

def quitarPasajero(num):
    rut_pasajeros.remove(num);
    return num;

def titulo():
    print("\n\t El Bote a Remos\n***********************************");

def rutValid():
    while True:
        try:
            rut_pasajero=int(input("Ingrese el RUN del pasajero: "));
            print("\n***********************************");
            long_rut = len(str(rut_pasajero));
            if (long_rut > 7 and long_rut < 10):
                return rut_pasajero;
            else:
                print("El RUN Ingresado es Erroneo");
        except ValueError:
            print("Debes Ingresar un RUT valido");

def optionValid():
    while True:
        try:
            op=int(input("Escriba una de las Opciones: "));
            if (op > 0 and op < 7):
                return op;
            else:
                print("La Opcion no se encuentra en la lista");
        except ValueError:
            print("Debes Ingresar un Numero de las Opciones");

def menu(matriz, matrizb):
    total_pagar=0;
    while True:
        titulo();
        print("(1) Mostrar Camarotes Disponibles\n(2) Comprar Boleto\n(3) Totales\n(4) Anular venta\n(5) Listado de pasajeros\n(6) Salir\n***********************************");
        op = optionValid();

        if (op == 1):
            titulo();
            mostrarMatriz(matriz);

        if (op == 2):
            titulo();
            asiento = asientoValid();
            rut_pasajero=rutValid();

            rellenarPasajero(matrizb, asiento, rut_pasajero);
            total_pagar += rellenarAsiento(matriz, asiento, rut_pasajero);
        
        if (op == 3):
            titulo();
            print("\tInforme de Ventas");
            print("Camarotes Vip\t\t=> ", len(vips));
            print("Camarotes Normales\t=> ", len(normales));
            print("Total, recaudado\t=> ", total_pagar, "\n***********************************");

        if (op == 4):
            titulo();
            asiento = asientoValid();

            eliminarPasajero(matrizb, asiento);
            total_pagar -= eliminarAsiento(matriz, matrizb, asiento);

        if (op == 5):
            titulo();
            if (len(rut_pasajeros) == 0):
                print("No hay Pasajeros");
            else:
                pasajeros = sorted(rut_pasajeros, key=int, reverse=False); 
                print("Lista actual de Pasajeros");
                for pasajero in pasajeros:
                    print("   -",pasajero);
                print("***********************************");
        
        if (op == 6):
            titulo();
            print("Regrese PRONTO", "\n***********************************");
            break;

        os.system("pause");
    return op;
