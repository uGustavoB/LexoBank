import socket

class BankClient:
    '''
    Classe para gerenciar a conexão com um servidor de banco usando sockets
    '''
    def __init__(self, host="localhost", port=9999):
        '''
        Inicializa a conexão com o servidor

        Se a conexão falhar, a conexão é definida como None
        '''
        try:
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP/IP
            self.cliente.connect((host, port)) # Conecta ao servidor
            print("Conectado ao servidor com sucesso.")
        except socket.error:
            print("Erro: Não foi possível conectar ao servidor. Verifique se o servidor está ativo.")
            self.cliente = None # Define como None para indicar que a conexão falhou
                                # Fazendo isso a gente consegue fazer a verificação do estado da conexão em outros métodos

    def enviar_requisicao(self, requisicao):
        '''
        Envia uma requisão para o servidor e imprime a resposta

        Levanta uma exceção se ocorrer um erro ao enviar a requisição 
        '''
        if self.cliente:
            try:
                self.cliente.send(requisicao.encode()) # Envia a requisição codificada
                response = self.cliente.recv(4096).decode() # Recebe a resposta do servidor

                partes = response.split(",", 1)
                codigo = int(partes[0].strip())
                mensagem = partes[1].strip() if len(partes) > 1 else None
                
                resultado_mensagem = self.obter_mensagem(codigo, mensagem)
                if resultado_mensagem:
                    print(resultado_mensagem)
                else:
                    print(mensagem)
            except socket.error:
                print(f"Erro ao enviar a requisição: verifique se o servidor está ativo.")
        else:
            print("Não há conexão com o servidor: verifique se o servidor está ativo.")

    def fechar_conexao(self):
        '''
        Fecha a conexão com o servidor, se estiver aberta
        '''
        if self.cliente:
            self.cliente.close() # Fecha a conexão 
            print("Conexão encerrada.")
        else:
            print("Nenhuma conexão para fechar.")

    def obter_mensagem(self, codigo:int, mensagem:str=None):
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
            # Gustavo - Adicionado mensagem de erro genérica
            404: "Erro desconhecido."
        }
        
        # Gustavo - Adicionado verificação para retornar a mensagem de erro personalizada
        if codigo == 404 or codigo == 200:
            return mensagem if mensagem else None
        return mensagens.get(codigo, mensagem if mensagem else None)

    def pausa_interacao(self):
        """
        Pausa a execução até que o usuário pressione Enter.
        """
        input("\nPressione Enter para continuar...")