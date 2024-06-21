# Deixar função parametrizado

valor_1 = 1
valor_2 = 3.5

valor_4 = 6
valor_5 = 4


def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    Uma função simples que retorna o valor de uma soma de valores
    """
    valor_3_resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return valor_3_resultado_da_soma


valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_4, valor_5)

print(valor_6)
