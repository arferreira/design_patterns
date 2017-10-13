from impostos import calcula_iss, calcula_icms

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento) 
        print("Imposto calculado: %.2f" % imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento, calcula_iss)
    calculador.realiza_calculo(orcamento, calcula_icms)
