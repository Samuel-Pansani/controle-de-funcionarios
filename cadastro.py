import funcoes

# Cria uma lista vazia para guardar os nomes dos funcionários
funcionarios = []
ids = 1

while True:
    # Interação com o usuário
    input('Pressione ENTER para continuar: ')

    # Mensagem de boas vindas
    print("\n=== Sistema de Cadastro de Funcionários ===")
    

    print('\n1 - Listar funcionários\n2 - Cadastrar funcionários\n3 - Pesquisar funcionário\n4 - Atualizar funcionário\n5 - Excluir funcionário\n6 - Salvar dados\n7 - Sair do sistema')

    # Escolha da operação
    operacao = str(input('\nOque deseja fazer? '))

    if operacao == '1':
        funcoes.listar_funcionarios(funcionarios)
    elif operacao == '2':
        ids, funcionarios = funcoes.cadastrar_funcionario(ids, funcionarios)
    elif operacao == '3':
        id_busca = int(input("\nDigite o ID do funcionário que deseja consultar: "))
        funcoes.consultar_funcionario(id_busca, funcionarios)
    elif operacao == '4':
        id_atualizar = int(input("\nQual ID do funcionário que deseja alterar as informações? "))
        funcoes.atualizar_funcionario(id_atualizar, funcionarios)
    elif operacao == '5':
        id_excluir = int(input('\nQual ID do funcionário que deseja excluir? '))
        funcoes.excluir_funcionario(id_excluir, funcionarios)
    elif operacao == '6':
        funcoes.salvar_dados(funcionarios)
    else:
        sair = input('\nVocê deseja mesmo sair? (s/n)').lower()
        if sair == 's':
            break