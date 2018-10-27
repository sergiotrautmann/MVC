class View:

    def __init__(self):
        self.control = None

    def set_control(self, control):
        self.control = control

    def exibir_menu(self):
        resposta = True
        while resposta:
            print('''
            1. Exibir lista
            2. Incluir item
            3. Excluir item
            4. Sair
            ''')

            resposta = int(input('Digite um número:'))

            if resposta == 1:
                print('\n Lista de itens')
                self.exibir_lista_compras(self.control.get_lista_compras())
            elif resposta == 2:
               self.control.add_item_lista()
               print('\n Item incluído')
            elif resposta == 3:
                self.control.remove_item_lista()
                print('\n Item excluído')
            elif resposta == 4:
                print('Vlw! Falou!')
                self.control.salvar_arquivo()
                resposta = False
            else:
                print('\n Valor incorreto!')

    def exibir_lista_compras(self, lista_compras):
        for chave, valor in lista_compras.items():
            print(f'\n- {chave} : {valor}')