<h1 align="center">Projeto LexoBank</h1>

## Descrição

Olá a todos! Sejam bem-vindos ao nosso projeto das disciplinas `Estruturas de Dados` e `Protocolos de Interconexão de Redes de Computadores`, do curso Sistemas para Internet no Instituto Federal de Educação, Ciência e Tecnologia da Paraíba.

A aplicação consiste em um sistema bancário que conta com uma arquitetura cliente-servidor, usando a linguagem Python. O cliente pode se conectar a um servidor, sendo ele em uma máquina local ou remota(testado apenas em rede local), e realizar operações bancárias básicas. O servidor é responsável por armazenar os dados dos clientes, como nome, saldo e histórico de transações.

O sistema foi projetado para demonstrar conceitos de programação de rede, estruturas de dados e algoritmos, e o uso de sockets para a comunicação entre o cliente e o servidor.


## Funcionalidades

- __Criação de contas__
- __Saldo__
- __Depósito__
- __Saque__
- __Transferência__
- __Histórico__

## Protocolo de comunicação criado

O protocolo de comunicação do sistema foi projetado para facilitar a interação entre o cliente e o servidor, permitindo que os usuários executem diversas operações bancárias. Cada requisição do cliente é uma string formatada que contém um comando específico seguido pelos argumentos necessários.

### Comandos disponíveis

- __CREATE \<numero_conta> \<saldo_inicial>__: Cria uma nova conta com um número de conta e um saldo inicial.
- __BALANCE \<numero_conta>__: Consulta o saldo de uma conta específica.
- __DEPOSIT \<numero_conta> \<valor>__: Realiza um depósito em uma conta.
- __WITHDRAW \<numero_conta> \<valor>__: Realiza um saque de uma conta.
- __TRANSFER \<conta_origem> \<conta_destino> \<valor>__: Transfere um valor de uma conta para outra.
- __HISTORY \<numero_conta>__: Retorna o histórico de transações de uma conta.

### Respostas do servidor

- __200__: Operação realizada com sucesso.
- __201__: Conta criada com sucesso.
- __300__: Conta não encontrada.
- __301__: Conta já existe.
- __302__: O destino deve ser uma instância de Conta.
- __303__: Não é possível transferir para a mesma conta.
- __304__: Saldo insuficiente.
- __305__: Saldo inicial não pode ser negativo.
- __306__: O valor do depósito deve ser positivo.
- __307__: O valor do saque deve ser maior que zero.
- __308__: O valor da transferência deve ser positivo.
- __404__: Erro desconhecido.



## Bibliotecas utilizadas

- __Socket:__ Empregada para a comunicação entre o cliente e o servidor.
- __Threading:__ Usada para a execução de múltiplas threads no servidor.
- __Os:__ Utilizada para limpeza do terminal.
- __Ast:__ Utilizada para conversão de strings em tuplas.

## Estruturas de dados utilizadas

- __Árvore AVL:__ Utilizada para armazenar as contas bancárias, permitindo a busca, inserção e remoção de contas de forma eficiente.
- __Pilha:__ Utilizada para armazenar o histórico de transações de uma conta, permitindo a adição e remoção de elementos no topo da pilha.

## Instruções

O projeto pode ser executado em seu computador localmente. Para isso, siga as instruções abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/uGustavoB/LexoBank.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd LexoBank
    ```

3. Inicie o servidor:
    ```bash
      python3 servidor.py
    ```

4. Inicie o cliente em outro terminal:
    ```bash
      python3 cliente.py
    ```

## Descrição dos arquivos

<!-- em tabelas -->

| Arquivo | Descrição |
| --- | --- |
| `cliente.py` | Cria uma instância de `BankClient` e apresenta um menu para que o usuário possa realizar as operações bancárias, enviando essas requisições para o servidor. |
| `servidor.py` | Escuta as conexões dos clientes, processando suas requisições e enviando-as para o gerenciador de contas, retornando respostas apropriadas. |
| `gerenciadorContas.py` | Classe que gerencia as contas bancárias, realizando operações como criar conta, depositar, sacar, transferir e obter saldo e histórico. |
| `conta.py` | Classe que representa uma conta bancária individual. Possuindo o número da conta, seu saldo, e histórico de movimentações. |
| `bankClient.py` | Gerencia as comunicações com o servidor. Ele estabelece as conexões, envia solicitações de operações bancárias e processa as respostas do servidor. |
| `protocolo.py` | Define o protocolo de comunicação entre o cliente e o servidor. Processa uma requisição recebida e retorna a resposta correspondente. |
| `avlTree.py` | Implemenentação de uma `árvore AVL`. Utilizada para guardar as contas, fazendo que seu gerenciamento seja realizado de forma rápida e eficiente. |
| `pilhaEncadeada.py` | Implementação de uma `pilha`. Utilizada para guardar o histórico de movimentações de uma conta na ordem da mais recente para mais antiga. |

## Autores

Este projeto foi desenvolvido por:

- __Gustavo Gabriel__ - [GitHub](https://github.com/uGustavoB)
- __Igor Miranda__ - [GitHub](https://github.com/imigoor)

