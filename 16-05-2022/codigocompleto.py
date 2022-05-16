import os;
os.system("color 6");
os.system("cls");

def problema6():
  tipo_usuario=0
  tipo_horario=0
  nombre_tipo_usuario=""
  nombre_tipo_horario=""
  precio_hora_normal=0
  precio_hora_punta=0
  print("Ingresa un el Tipo de Horario (1. Horario Normal, 2. Horario Punta)");
  tipo_horario=int(input());
  print("Ingresa un el Tipo de Usuario (1. para Joven, 2. para Adulto, 3. para Adulto Mayor)");
  tipo_usuario=int(input());
  continuar=True
  
  while (continuar):
    precio_hora_normal = 490;
    precio_hora_punta = 590;
    if (tipo_horario == 1):
      nombre_tipo_horario = "Horario Normal";
    else:
      nombre_tipo_horario = "Horario Punta";

    if (tipo_usuario == 1):
      nombre_tipo_usuario = "Joven";
    elif (tipo_usuario == 2):
      nombre_tipo_usuario = "Adulto";
      precio_hora_normal += 300
      precio_hora_punta += 300
    elif (tipo_usuario == 3):
      nombre_tipo_usuario = "Adulto Mayor";
      precio_hora_normal -= 100
      precio_hora_punta -= 100
    continuar=False

  print("Tipo de Horario", nombre_tipo_horario);
  if (tipo_horario == 1):
    print("Total a Pagar" , precio_hora_normal);
  if (tipo_horario == 2):
    print("Total a Pagar" , precio_hora_punta);
problema6();
