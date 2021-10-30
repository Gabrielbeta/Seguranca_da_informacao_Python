import socket # biblioteca que lida com a placa de rede
import sys  # dá acesso a variáveis e funções do interpretador 
 
def main(): # estamos criando a função main para testar uma coneçãi TCP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # estamos acessando o método socket (dentro da classe socket),  o AF_INET estamos dizendo que vamos usar o protocolo IP
        # O SOCK_STREAM informa que vamos usar o TCP e o número 0 significa que é o protocolo TCP
    except socket.error as e: # se der um errro na conexão chamaremos o erro de "e"

        print("A conexão falhou!!!")
        print("Erro: {}".format(e)) # se der um erro ele imprime o erro
        sys.exit() # O exit é para fechar o programa todo

    print("Socket criado com sucesso") # caso for feita a conexão ele printa sucesso

                            # O usuário vai digitar o IP do site e a porta
    HostAlvo = input("Digite o Host ou IP a ser conectado: ") 
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo))) # o connect faz a conecção e pede 2 parâmetros mas a porta precisa ser um valor inteiro (não string) / a quantidade de parentes é importante
        print(f"Cliente TCP conectado com sucesso no Host: {HostAlvo} \n Porta: {PortaAlvo}")
        s.shutdown(2) # para não ficar em looping estamos pedindo para fechar a aplicação depois de 2 segundos
    except socket.error as e:
        print(f"Não foi possível conectar no Host: {HostAlvo} \n Porta: {PortaAlvo}")
        print(f"Erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main() 