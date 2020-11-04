

def cadastros():
    nome = input("nome:")
    while(len(nome)<3):
        print ( "O nome deve conter no mínimo 3 letras " )
        nome = input("nome: ")
    sobrenome = input("sobrenome : ")
    while(len(sobrenome)<3):
        print ( "O sobrenome deve conter no mínimo 3 letras" )
        sobrenome = input("sobrenome: ")
        senha = input("Sua senha: ")
    while ((len(senha)<5 ) or (senha.isalnum() == True or senha.isalpha() == True )):
        senha = input("Digite novamente a senha:")
    endereco = input("Informe seu endereço : ")
    celular = int(input("Informe seu número de telefone : "))
    cpf = int(input("Informe seu CPF : "))
    numero  =  0
    while(numero == 0):
        email = input("Informe seu E-mail : ")
        if "@" in email :
            print("E-mail cadastrado")
            numero = 1

def  módulos():
    caixa  =  1
    saldoTotal  =  0
    contaTransferencia  =  0
    sacar  =  0
    while  caixa  ==  1 :
    
        print ( "Digite 1 para deposito" )
        print ( "Digite 2 para  saque" )
        print ( "Digite 3 para exibir saldo" )
        print ( "Digite 4 para download" )
        print ( "Digite 5 para encerrar conta" )    
        escolha  =  int ( input ( "Deseja realizar qual operação:"))
    
    if  escolha  ==  1 :
        depositar  =  int ( input ( "Valor do depósito:" ))
        while  depositar  <  0 :
             depositar  =  int ( input ( "O depósito deve no mínimo ser de R$ 1,00: " ))
             print ( "Seu saldo atual é:" , saldoTotal )
    else :
        saldoTotal  =  depositar  +  saldoTotal
        print ( "Seu saldo atual é:" , saldoTotal )
    if  escolha  ==  2 :
        sacar  =  float ( input ( " Valor do saque:" ))
        while  sacar  >  saldoTotal :
            print ( "Voce não possui saldo suficiente para esta operação! Insira um valor menor que:" , saldoTotal , "" )
        escolha  =  int ( input ( "Escolha outra operação:" ))
    else :
        saldoTotal  =  saldoTotal  -  sacar
        print ( " saldo atual: " , saldoTotal )      
    if  escolha  ==  3 :
            print ( "saldo atual:" , saldoTotal )    
    if  escolha  ==  4 :
     contaTransferencia  =  int ( input ( " Endereço de conta para realizar a transferência:" ))
     transferencia  =  int ( input ( "Valor a ser transferido:" ))
    if  transferencia  >  saldoTotal :
          print ( "saldo insuficiente para essa tranferencia! Insira um valor menor que:" , saldoTotal , "" )
    else :
          saldoTotal  =  saldoTotal  -  transferencia 
          contaTransferencia  =  contaTransferencia  +  transferencia 
          print ( "tranferencia realizada com succeso:" )
          print ( "Seu saldo é de:" , saldoTotal )
    if  escolha  ==  5 :
        print ( "Operação encerrada!" )
        caixa  =  0 
            
def  parteAtualização ():
    saldoTotal = 0
    novaEscolha  =  0
    atualizarCadastro  =  0
    while ( atualizarCadastro  ==  0 ):
        print ( " 1 para consultar um cliente" )
        print ( " 2 para consultar uma lista de clientes" )
        print ( " 3 para deletar um cliente" )
        print ( " 4 para atualizar dados de um cliente específico" )
        print ( " 5 para encerrar" )
        novaEscolha  =  int ( input ( "escolha a operação:" ))
        if  novaEscolha  ==  1 :
            numerocliente =  int ( input ( "Numero do cliente no cadastro:" ))
            print ( "Nome do cliente:" , nome [ numerocliente ])  
            print ( "Sobrenome do cliente:" , sobrenome [ numerocliente ])
            print ( "Endereço do cliente:" , endereco [ numerocliente ])
            print ( "Numero do cliente:" , celular [ numerocliente ])
            print ( "Cpf do cliente:" , cpf [ numerocliente ])
            print ( "E-mail do cliente:" , email [ numerocliente ])
            print ( "Senha do cliente:" , senha [ numerocliente ])
        if  novaEscolha  ==  2 :
            print ( "Lista de clientes:" , nome )
        if  novaEscolha  ==  3 :
            númeroexcluir  =  int ( input ( "Numero do cliente que voce deseja excluir:" ))
            del ( nome [ númeroexcluir ])
            del ( sobrenome [ númeroexcluir ])
            del ( cpf[ númeroexcluir ])
            del ( email [ númeroexcluir ])
            del ( endereco [ númeroexcluir ])
            del ( numero [ númeroexcluir ])
            del ( senha [ númeroexcluir ])
        
        if  novaEscolha  ==  4 :
            atualizarCadastro  =  0
            numeroCliente = int ( input ( "Numero de cadastro do cliente que voce deseja modificar:" ))
            nome . insert ( numerocliente , ( input ( "nome:" )))  
            while(len(nome)<3):
                print ( "O nome deve conter no mínimo 3 letras " )
                nome = input("nome: ")
            sobrenome . inserir ( numerocliente , ( input ( "Insira seu sobrenome:" )))
            while(len(sobrenome)<3):
                print ( "O sobrenome deve conter no mínimo 3 letras" )
                sobrenome = input("sobrenome: ")
                sobrenome =input("Informe seu sobrenome, no mínimo 3 letras: ")
            celular . insert ( numerocliente , ( input ( "Digite um número para contato:" )))
            cpf . insert ( numerocliente , ( input ( "cpf:" )))
            endereco . insert ( numerocliente , ( input ( "endereço:" )))
            numeroo  =  0
            while(numeroo == 0):
                 email . append ( input ( "Digite seu email: " ))  
                 if "@" in email :
                    print("E-mail cadastrado")
                    numeroo = 1
            senha . anexar ( input ( "Digite sua senha, ela precisa conter caracteres especiais e numeros:" ))
            while ((len(senha)<5 ) or (senha.isalnum() == True or senha.isalpha() == True )):
                 senha = input("Digite novamente a senha:")
            if  novaEscolha  ==  5 :
                atualizarCadastro =  atualizarCadastro  +  1
cadastros ()
módulos()
parteAtualização ()     