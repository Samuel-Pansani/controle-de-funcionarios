def validar_nome():
    """ Função para validar nome - Não há parametros"""
    while True:
        nome = input("Digite o nome do funcionário: ")
        if nome.strip():
            return nome
        print("Nome não pode estar em branco. Tente novamente.")


def salvar_dados(funcionarios):
    """Cria um documento .txt para salvar os dados dos funcionários - Parametro de funcionarios"""
    with open("cadastro_funcionarios.txt", "w") as arquivo:
        arquivo.write("ID\tNome\t\tCargo\n")
        for func in funcionarios:
            arquivo.write(f"{func['id']}\t{func['nome']}\t\t{func['cargo']}\n")
    print('Dados salvos com sucesso!')


def consultar_funcionario(id_busca, funcionarios):
    """Pesquisa funcionário pela ID - (id, lista de funcionários)"""
    for func in funcionarios:
        if func['id'] == id_busca:
            print(f"ID: {func['id']} | Nome: {func['nome']} | Cargo: {func['cargo']}")
            return
    print("Funcionario não encontrado.")


def excluir_funcionario(id_excluir, funcionarios):
    """Exclui 1 funcionário - (id, lista de funcionários)"""
    for func in funcionarios:
        if func['id'] == id_excluir:
            confirmar = input(f"Tem certeza que deseja excluir {func['nome']}? (s/n): ")
            if confirmar.lower() == 's':
                funcionarios.remove(func)
                print("Funcionário excluído com sucesso.")
                return
            else:
                print("Exclusão cancelada.")
                return
    print("Funcionário não encontrado.")


def atualizar_funcionario(id_atualizar, funcionarios):
    """Atualiza os dados de 1 funcionário - (id, lista de funcionários)"""

    # Loop para encontrar o funcionário
    for func in funcionarios:
        if func['id'] == id_atualizar:

            # Pedido de confirmação
            confirmar = input(f"Deseja alterar os dados de {func['nome']}? (s/n): ")
            if confirmar.lower() == 's':

                # Qual dado deseja alterar (nome ou cargo)
                qual = input("Oque deseja alterar?\nC - Cargo\nN - Nome\n--> ").lower()
                if qual == 'c':
                    novo_cargo = input("Digite o novo nome de cargo: ")
                    func['cargo'] = novo_cargo

                    print(f"Cargo atualizado! Agora {func['nome']} é um {func['cargo']}!")
                    return
                else:
                    novo_nome = input("\nDigite o novo nome do usuário: ")
                    func['nome'] = novo_nome

                    print(f"Nome alterado para {func['nome']} com sucesso!\n")
                    return
            print('Alteração cancelada')
            return
    print('Funcionário não encontrado')


def listar_funcionarios(funcionarios):
    """Exibe uma lista final de nomes e cargos cadrastados"""
    print('\nFuncionários Cadastrados:')
    print(f'{'ID':<5} {'Nome':<20} {'Cargo':<20}')
    for funcionario in funcionarios:
        print(f'{funcionario['id']:<5} {funcionario['nome']:<20} {funcionario['cargo']:<20}')

def cadastrar_funcionario(ids, funcionarios):
    """Realiza o cadastro de funcionários - Precisa inserir (ids, lista dos funcionarios)"""
    # Pergunta quantos usuários deseja cadastrar
    quantidade = int(input("\nQuantos funcionários deseja cadastrar? "))

    # Loop para coletar os nomes dos funcionários e o respectivo cargo
    for i in range(quantidade):

        if i == 0:
            novos_funcionarios = []

        print(f'\nFuncionário nº{i + ids}')
        nome = validar_nome()

        if nome.strip() == "":
            print("Nome inválido. Tente novamente.")
            continue

        cargo = input('Digite o cargo do funcionário: ')
        funcionario = {'id': i + ids, 'nome': nome, 'cargo': cargo}

        novos_funcionarios.append(funcionario)

    ids += len(novos_funcionarios)
    funcionarios += novos_funcionarios

    print('\nOs seguintes funcionários foram cadastrados:')
    print(f'{'ID':<5} {'Nome':<20} {'Cargo':<20}')
    for funcionario in novos_funcionarios:
        print(f'{funcionario['id']:<5} {funcionario['nome']:<20} {funcionario['cargo']}')
    
    return ids, funcionarios