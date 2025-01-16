import socket
import random
frases = ["La vida es como montar en bicicleta. Despues de 6 horas, te duele el culo.",
    "El éxito es como salida en ingles pero en masculino.",
    "El único límite para alcanzar tus sueños es la cantidad de farlopa que consumas.",
    "Nunca es tarde para ducharse, otaku.",
    "El arte es morirte de frio.",
    "FELICIDADES!!! HAS GANADO UN iPHONE ULTIMO MODELO"]

# 1. Crear el socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

# 2. Enlazar el socket a una dirección y puerto

server_address = ('192.168.56.1', 2017)  # Dirección y puerto

server_socket.bind(server_address)

 

# 3. Poner el socket en modo escucha

server_socket.listen(5)  # Permite hasta 5 conexiones 

print(f"Servidor de 'Cita del Día' escuchando en {server_address}")

 
try:
    while True:

    # 4. Aceptar conexiones

        client_socket, client_address = server_socket.accept()

        print(f"Conexión aceptada de {client_address}")

    

    # 5. Manejar la conexión
        cita = random.choice(frases)
        data = client_socket.recv(1024).decode('utf-8')
        # Recibir datos
        client_socket.sendall(cita.encode('utf-8'))

        print(f"Datos recibidos: {data}\n")

        response = "\nMensaje recibido"

        client_socket.sendall(response.encode('utf-8'))  # Enviar respuesta

        

        # 6. Cerrar la conexión

        client_socket.close()
except Exception:
    print("\nServidor detenido.")
    server_socket.close()

    