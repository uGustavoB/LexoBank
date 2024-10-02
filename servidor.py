import socket
import threading
from gerenciadorContas import GerenciadorContas
from protocolo import processar_requisicao
 
class ServidorBanco:
    """
    Classe que representa um servidor de banco, permitindo a comunicação com clientes
    através de sockets. O servidor é responsável por aceitar conexões de clientes,
    gerenciar suas requisições e fornecer respostas apropriadas utilizando um 
    gerenciador de contas.

    Atributos:
        __servidor (socket.socket): Objeto socket que representa o servidor.
        __gerenciador (GerenciadorContas): Instância da classe GerenciadorContas,
            responsável pela gestão das contas bancárias utilizando Estrutura de Dados AVL.
        __tamanhoBuffer (int): Tamanho do buffer para a leitura de dados do cliente.
        endereco (tuple): Endereço IP e porta do cliente conectado.
    """
    
    def __init__(self, host: str = "0.0.0.0", port: int = 9999, tamanhoBuffer: int = 1024):
        '''
        Inicializa o servidor com o endereço IP e a porta.

        Parâmetros:
            host (str): Endereço IP do servidor, padrão é "0.0.0.0".
            port (int): Porta na qual o servidor irá escutar, padrão é 9999.
            tamanhoBuffer (int): Tamanho do buffer para recepção de dados, padrão é 1024 bytes.

        Atributos:
            __servidor (socket.socket): Objeto socket que representa o servidor.
            __gerenciador (GerenciadorContas): Instância da classe GerenciadorContas, responsável pela gestão das contas bancárias utilizando Estrutura de Dados AVL.
            __tamanhoBuffer (int): Tamanho do buffer para a leitura de dados do cliente.

        Ação:
            Inicializa um socket TCP, associa o socket ao endereço IP e porta fornecidos, 
            e prepara o servidor para escutar até 5 conexões simultâneas. O número de conexões pode ser
            ajustado dependendo do desempenho necessário.
        '''
        self.__servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um objeto socket
        self.__servidor.bind((host, port)) # Associa o socket ao endereço IP e porta fornecidos
        self.__servidor.listen(5)  # Configura para que o servidor escute até 5 conexões. Se for aumentar tem que verificar se pode afetar no desempenho
        self.__gerenciador = GerenciadorContas()
        self.__tamanhoBuffer = tamanhoBuffer

    def iniciar_servidor(self) -> None:
        '''
        Inicia o servidor e aguarda conexões de clientes.

        Este método entra em um loop infinito, onde aceita conexões de clientes e
        cria uma nova thread para gerenciar cada conexão. Trata erros relacionados
        à operação do servidor, permitindo que ele continue funcionando ou seja
        encerrado de maneira segura. 

        Exemplo de uso:
            servidor = ServidorBanco()
            servidor.iniciar_servidor()
        '''
        print("Servidor iniciado e aguardando conexões...")

        while True:
            try:
                cliente, self.endereco = self.__servidor.accept()  # Aceita uma conexão de um cliente
                print(f"Conexão estabelecida com {self.endereco}")

                cliente_thread = threading.Thread(target=self.__gerenciar_cliente, args=(cliente, self.endereco))
                cliente_thread.start()
            except socket.error:
                print(f"Ocorreu um erro no servidor. Verifique a conexão e tente novamente.")
            except KeyboardInterrupt:
                print("\nServidor encerrado.")
                break    

    def __gerenciar_cliente(self, cliente: socket.socket, endereco: tuple) -> None:
        '''
        Gerencia a comunicação com um cliente específico.

        Parâmetros:
            cliente (socket.socket): Objeto socket que representa a conexão com o cliente.
            endereco (tuple): Endereço IP e porta do cliente conectado.

        Este método recebe requisições do cliente em um loop, processa as requisições
        utilizando a função `processar_requisicao`, e envia as respostas de volta ao cliente.
        Trata erros de comunicação e garante o encerramento da conexão quando necessário.
        '''
        try:
            while True:
                requisicao = cliente.recv(self.__tamanhoBuffer).decode() # Recebe a requisição do cliente. O tamanho do buffer é de 4096 bytes

                if not requisicao:
                    break

                resposta = processar_requisicao(requisicao, self.__gerenciador) # Procesa a requisição recebida e obtém a resposta
                # Envia a resposta de volta para o cliente
                if resposta is not tuple:
                    print(resposta)
                    cliente.send(f"{resposta}".encode())
                else:
                    cliente.send(f"{resposta[0]},{resposta[1]}".encode())
        except socket.error:
            print(f"Erro na comunicação com o cliente. Conexão encerrada.")
        finally:
            cliente.close()
            print(f"Conexão com cliente {endereco} encerrada.")

if __name__ == "__main__":
    """
    Cria uma instância do servidor e inicia o servidor.
    
    Esse bloco é executado quando o script é rodado diretamente, iniciando o 
    servidor de banco que escutará por conexões de clientes.
    """
    servidor = ServidorBanco()
    servidor.iniciar_servidor()