class Pais:

    def __init__(self, nome):
        self.nome = nome
        self.dados = {}

    def toString(self):
        #', '.join("{!s}={!r}".format(key,val) for (key,val) in k.items())
        return 'Pais: nome='+self.nome+', dados='+str(self.dados)
    
    def print_top_n(self, n=None):
        n = self.topn if n is None else n
        print(n)