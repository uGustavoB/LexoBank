def processar_requisicao(requisicao, gerenciador_contas):
    '''
    Processa uma requisição recebida e retorna a resposta correspondente.

    :param requisicao: Comando recebido do cliente.
    :param gerenciador_contas: Instância do GerenciadorContas para manipulação das contas.
    :return: Resposta ao cliente.
    '''
    partes = requisicao.split()  # Divide a requisição em partes utilizando o espaço como delimitador

    try:
        if partes[0] == "CREATE":
            numero_conta = partes[1]
            saldo_inicial = float(partes[2])
            return gerenciador_contas.criar_conta(numero_conta, saldo_inicial)

        elif partes[0] == "BALANCE":
            numero_conta = partes[1]
            return gerenciador_contas.consultar_saldo(numero_conta)

        elif partes[0] == "DEPOSIT":
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.depositar(numero_conta, valor)

        elif partes[0] == "WITHDRAW":
            numero_conta = partes[1]
            valor = float(partes[2])
            return gerenciador_contas.sacar(numero_conta, valor)

        elif partes[0] == "TRANSFER":
            conta_origem = partes[1]
            conta_destino = partes[2]
            valor = float(partes[3])
            return gerenciador_contas.transferir(conta_origem, conta_destino, valor)

        elif partes[0] == "HISTORY":
            numero_conta = partes[1]
            return gerenciador_contas.historico(numero_conta)

        return "Comando inválido."
    except Exception as e:
        return f"Erro ao processar requisição: {e}"