import socket
import ast

class BankClient:
    '''
    Classe para gerenciar a comunicação com um servidor de banco usando sockets.

    Essa classe permite que o cliente se conecte a um servidor, envie solicitações e receba respostas,
    além de interpretar os códigos de resposta do servidor e fechar a conexão de forma segura.

    Atributos:
        cliente (socket.socket): Objeto socket que representa a conexão com o servidor. É inicializado
        no método `__init__` e utilizado nos métodos `enviar_requisicao` e `fechar_conexao`.
    '''
    def __init__(self, host="localhost", port=9998, tamanhoBuffer=1024):
        '''
        Inicializa a conexão com o servidor de banco.

        O método tenta estabelecer uma conexão TCP/IP com o servidor usando o endereço e porta fornecidos.
        Em caso de erro na conexão, a conexão é marcada como `None` para evitar problemas nos outros métodos
        que dependem da existência da conexão.

        Parâmetros:
            host (str): Endereço do servidor. O padrão é "localhost".
            port (int): Porta na qual o servidor está escutando. O padrão é 9999.

        Exceções:
            socket.error: Captura erros de conexão e informa que a conexão falhou.
        '''

        self.__tamanhoBuffer = tamanhoBuffer
        try:
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP/IP
            self.cliente.settimeout(5) # Define um tempo limite de 5 segundos para a conexão
            self.cliente.connect((host, port)) # Conecta ao servidor
            print("Conectado ao servidor com sucesso.")
        except socket.error:
            print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está ativo.")
            self.cliente = None # Define como None para indicar que a conexão falhou
                                # Fazendo isso a gente consegue fazer a verificação do estado da conexão em outros métodos

    def enviar_requisicao(self, requisicao):
        '''
        Envia uma requisição para o servidor e lida com a resposta.

        O método envia uma requisição codificada ao servidor. Em seguida, espera uma resposta e processa o código 
        de status retornado junto com a mensagem. Se o código de status for reconhecido, uma mensagem apropriada 
        é exibida. Caso contrário, é apresentada a mensagem original recebida.

        Parâmetros:
            requisicao (str): A string que representa a solicitação a ser enviada para o servidor.

        Exceções:
            socket.error: Caso ocorra um erro ao enviar ou receber a requisição, será informado ao usuário.

        Exemplo:
            cliente.enviar_requisicao("CREATE 12345 1000.0")
        '''
        if self.cliente:
            try:
                self.cliente.send(requisicao.encode()) # Envia a requisição codificada
                response = ast.literal_eval(self.cliente.recv(self.__tamanhoBuffer).decode()) # Recebe a resposta do servidor
                # print(response)
                if type(response) is tuple:
                    codigo, mensagem = response
                else:
                    codigo, mensagem = response, None
                
                # print(codigo, mensagem)
                # partes = response.split(",", 1)
                # codigo = int(partes[0].strip())
                # mensagem = partes[1].strip() if len(partes) > 1 else None
                
                resultado_mensagem = self.obter_mensagem(codigo, mensagem)
                if resultado_mensagem:
                    print(resultado_mensagem)
                else:
                    print(mensagem)
            except socket.error:
                print(f"Erro ao enviar a requisição. Verifique se o servidor está ativo.")
        else:
            print("Não há conexão com o servidor. Verifique se o servidor está ativo.")

    def obter_mensagem(self, codigo: int, mensagem: str = None):
        '''
        Retorna uma mensagem correspondente ao código de status recebido do servidor.

        Esse método mapeia códigos de status recebidos do servidor para mensagens amigáveis ao usuário.
        Para códigos de status conhecidos, retorna uma mensagem pré-definida. Para o código 404, retorna
        a mensagem personalizada fornecida pelo servidor, se disponível.

        Parâmetros:
            codigo (int): O código de status retornado pelo servidor.
            mensagem (str): Mensagem opcional personalizada retornada pelo servidor.

        Retorna:
            str: Mensagem amigável ao usuário baseada no código de status, ou `None` se o código for desconhecido.

        Exemplo:
            client.obter_mensagem(200)  # Retorna "Operação realizada com sucesso"
        '''
        mensagens = {
            200: "Operação realizada com sucesso",
            201: "Conta criada com sucesso",
            300: "Conta não encontrada",
            301: "Conta já existe",
            302: "O destino deve ser uma instância de Conta",
            303: "Não é possível transferir para a mesma conta",
            304: "Saldo insuficiente",
            305: "Saldo inicial não pode ser negativo",
            306: "O valor do depósito deve ser positivo",
            307: "O valor do saque deve ser maior que zero",
            308: "O valor da transferência deve ser positivo",
            # Adicionado mensagem de erro genérica
            404: "Erro desconhecido."
        }
        
        # Adicionado verificação para retornar a mensagem de erro personalizada
        if codigo == 404:
            return mensagem if mensagem else None
        if codigo == 200:
            return mensagem if mensagem else mensagens.get(codigo, None)
        return mensagens.get(codigo, mensagem if mensagem else None)
    
    def fechar_conexao(self):
        '''
        Fecha a conexão com o servidor, caso esteja aberta.

        Se o cliente tiver uma conexão aberta com o servidor, ela será fechada com segurança. Caso contrário,
        uma mensagem informando que não há conexão será exibida.

        Exemplo:
            client.fechar_conexao()
        '''
        if self.cliente:
            self.cliente.close()
            print("Conexão encerrada.")
        else:
            print("Nenhuma conexão para fechar.")

    def pausa_interacao(self):
        """
        Pausa a execução do programa até que o usuário pressione Enter.

        Esse método é útil para manter o programa em execução até que o usuário esteja pronto para continuar,
        permitindo que o usuário visualize as informações antes que o programa prossiga.

        Exemplo:
            cliente.pausa_interacao()
        """
        input("\nPressione Enter para continuar...")