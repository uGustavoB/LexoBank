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
                print(response)
            except socket.error as e:
                print(f"Erro ao enviar a requisição: {e}")
        else:
            print("Não há conexão com o servidor. Verifique se o servidor está ativo.")

    def fechar_conexao(self):
        '''
        Fecha a conexão com o servidor, se estiver aberta
        '''
        if self.cliente:
            self.cliente.close() # Fecha a conexão 
            print("Conexão encerrada.")
        else:
            print("Nenhuma conexão para fechar.")

    def pausa_interacao(self):
        """
        Pausa a execução até que o usuário pressione Enter.
        """
        input("\nPressione Enter para continuar...")