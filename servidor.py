import socket
import threading
from gerenciadorContas import GerenciadorContas
from protocolo import processar_requisicao
 
class ServidorBanco:
    def __init__(self, host="localhost", port=9999):
        '''
        Inicializa o servidor com o endereço IP e a porta.
        '''
        self.__servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um objeto socket
        self.__servidor.bind((host, port)) # Associa o socket ao endereço IP e porta fornecidos
        self.__servidor.listen(5)  # Configura para que o servidor escute até 5 conexões. Se for aumentar tem que verificar se pode afetar no desempenho
        self.__gerenciador = GerenciadorContas()  # Usa a AVL e a Pilha Encadeada

    def iniciar_servidor(self):
        '''
        Inicia o servidor e aguarda conexões de clientes
        '''
        print("Servidor iniciado e aguardando conexões...")

        while True:
            try:
                # Aceita uma conexão de um cliente.
                cliente, self.endereco = self.__servidor.accept()
                print(f"Conexão estabelecida com {self.endereco}")

                # Aqui vai gerenciar a comunicação com o cliente conectado
                cliente_thread = threading.Thread(target=self.__gerenciar_cliente, args=(cliente, self.endereco))
                cliente_thread.start()
            except socket.error as e:
                # Captura e exibe erros relacionados à opreção do servidor
                print(f"Erro no servidor: {e}")
            except KeyboardInterrupt:
                print("\nServidor encerrado.")
                break

    def __gerenciar_cliente(self, cliente, endereco):
        '''
        Gerencia a comunicação com um cliente específico.
        '''
        try:
            while True:
                # Recebe a requisição do cliente. O tamanho do buffer é de 4096 bytes.
                requisicao = cliente.recv(4096).decode()

                # Se não houver dados recebidos, encerra a comunicação com o cliente
                if not requisicao:
                    break

                # Processa a requisição recebida e obtém a resposta
                resposta = processar_requisicao(requisicao, self.__gerenciador)

                # Envia a resposta de volta para o cliente
                cliente.send(resposta.encode())
        except socket.error as e:
            # Captura e exibe erros relacionados à comunicação com o cliente
            print(f"Erro na comunicação com o cliente: {e}")
        finally:
            # Este bloco é sempre executado, independentemente de uma exceção ocorrer ou não
            cliente.close() # Fecha a conexão com o cliente
            print(f"Conexão com cliente {self.endereco} encerrada.")

if __name__ == "__main__":
    # Cria uma instância do servidor e inicia o servidor
    servidor = ServidorBanco()
    servidor.iniciar_servidor()