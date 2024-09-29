def processar_requisicao(requisicao, gerenciador_contas):
    '''
    Processa uma requisição recebida e retorna a resposta correspondente.

    Parâmetros:
        requisicao (str): Comando recebido do cliente, contendo o tipo de operação e argumento.
        gerenciador_contas (GerenciadorContas): Instância do GerenciadorContas para manipulação das contas.

    Returns:
        tuple: Resposta ao cliente com uma tupla (código, mesagem).
            O código indica o status da operação e a mensagem fornece detalhes adicionais

    Exemplos de uso:
        resposta = processar_requisicao("CREATE 12345 1000.0")
        print(resposta) (201, None)
    '''
    partes = requisicao.split()  # Divide a requisição em partes utilizando o espaço como delimitador
    
    def check_erro(quantidade: int):
        '''
        Verifica se a quantidade de argumentos passados é a esperada.

        Parâmetros:
            quantidade (int): Número esperado de argumentos na requisição.
        
        Retorna:
            bool: Retorna True se a quantidade estiver errada, caso contrário False.
        '''
        if len(partes) != quantidade:
            return True
    
    def mensagem_erro_quantidade(esperado: int):
        '''
        Gera uma mensagem de erro informando a quantidade de argumentos incorreta.

        Parâmetros:
            esperado (int): Número esperado de argumentos.

        Retorna:
            str: Mensagem de erro formatada.
        '''
        return f"Quantidade de argumentos incorreta. Esperado: {esperado}. Recebido: {len(partes) - 1}"

    try:
        if partes[0] == "CREATE":
            if check_erro(3):
                # Gustavo - Tentar resolver posteriormente as repetições da mensagem de erro
                return 404, mensagem_erro_quantidade(2)
            numero_conta = partes[1]
            saldo_inicial = float(partes[2])
            return gerenciador_contas.criar_conta(numero_conta, saldo_inicial)

        elif partes[0] == "BALANCE":
            if check_erro(2):
                return 404, mensagem_erro_quantidade(1)
            numero_conta = partes[1]
            return gerenciador_contas.consultar_saldo(numero_conta)

        elif partes[0] == "DEPOSIT":
            if check_erro(3):
                return 404, mensagem_erro_quantidade(2)
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.depositar(numero_conta, valor)

        elif partes[0] == "WITHDRAW":
            if check_erro(3):
                return 404, mensagem_erro_quantidade(2)
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.sacar(numero_conta, valor)

        elif partes[0] == "TRANSFER":
            if check_erro(4):
                return 404, mensagem_erro_quantidade(3)
            conta_origem = partes[1]
            conta_destino = partes[2]
            valor = float(partes[3])
            return gerenciador_contas.transferir(conta_origem, conta_destino, valor)

        elif partes[0] == "HISTORY":
            if check_erro(2):
                return 404, mensagem_erro_quantidade(1)
            numero_conta = partes[1]
            return gerenciador_contas.historico(numero_conta)

        return None, "Comando não reconhecido."  # Retorna um código de erro genérico

    except ValueError as e:
        return str(e), None  # Retorna erro de argumento