from arquivo import Arquivo
class Control:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.carregar_lista_compras()
    def exibir_menu(self):
        self.view.exibir_menu()

    def get_lista_compras(self):
        return self.model.lista_compras

    def add_item_lista(self):
        chave = input('Digite o item:')
        valor = int(input('Digite a quantidade:'))
        if self.get_chave(chave) == None:
            self.model.lista_compras.update({chave: valor})
        else:
            self.model.lista_compras[chave] += valor

    def remove_item_lista(self):
        chave = input('Digite o item a ser excluido')
        self.model.lista_compras.pop(chave)


    def get_chave(self, chave):
        return self.model.lista_compras.get(chave)

    def carregar_lista_compras(self):
        a = Arquivo()
        self.model.carregar_lista_compras(a.ler_arquivo())

    def salvar_arquivo(self):
        a =Arquivo()
        a.salvar_arquivo(self.model.lista_compras)