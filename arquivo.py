class Arquivo:
    def __init__(self):
        self.lista = None

    def ler_arquivo(self):
        lis = open('lista.txt', 'r+')
        lista = lis.readlines()
        dict = {}
        for item in lista:
            ll = item.split(':')
            key = str(ll[0])
            value = int(ll[1])
            dict[key] = value
        self.lista = dict
        return self.lista

    def salvar_arquivo(self, lista_compras):
        lis = open('lista.txt', 'w')
        for chave, valor in lista_compras.items():
            c =  chave + ':' + str(valor) + '\n'
            lis.writelines(c)
        lis.close()