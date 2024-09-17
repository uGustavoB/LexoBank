def processar_requisicao(requisicao, gerenciador_contas):
    '''
    Processa uma requisição recebida e retorna a resposta correspondente.

    :param requisicao: Comando recebido do cliente.
    :param gerenciador_contas: Instância do GerenciadorContas para manipulação das contas.
    :return: Resposta ao cliente.
    '''
    partes = requisicao.split()  # Divide a requisição em partes utilizando o espaço como delimitador
    
    def check_erro(quantidade: int):
        '''
        Verifica se a quantidade de argumentos passados é a esperada.
        '''
        if len(partes) != quantidade:
            raise ValueError(f"Quantidade de argumentos incorreta. Esperado: {quantidade-1}. Recebido: {len(partes)-1}")
        

    try:
        if partes[0] == "CREATE":
            check_erro(3)
            numero_conta = partes[1]
            saldo_inicial = float(partes[2])
            return gerenciador_contas.criar_conta(numero_conta, saldo_inicial)

        elif partes[0] == "BALANCE":
            check_erro(2)
            numero_conta = partes[1]
            return gerenciador_contas.consultar_saldo(numero_conta)

        elif partes[0] == "DEPOSIT":
            check_erro(3)
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.depositar(numero_conta, valor)

        elif partes[0] == "WITHDRAW":
            check_erro(3)
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.sacar(numero_conta, valor)

        elif partes[0] == "TRANSFER":
            check_erro(4)
            conta_origem = partes[1]
            conta_destino = partes[2]
            valor = float(partes[3])
            return gerenciador_contas.transferir(conta_origem, conta_destino, valor)

        elif partes[0] == "HISTORY":
            check_erro(2)
            numero_conta = partes[1]
            return gerenciador_contas.historico(numero_conta)

        return False
    except ValueError as e:
        return str(e)