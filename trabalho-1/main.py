# -*- coding: utf-8 -*-
from sympy import *


def novo_intervalo(y, intervalo, x3):
    y1 = y.subs(x, intervalo[0]).evalf()
    y3 = y.subs(x, x3).evalf()

    if (y1 * y3 < 0):
        return [intervalo[0], x3]
    return [intervalo[1], x3]


def derivada_funcao_no_ponto(y, ponto, casas_decimais):
    derivada = y.diff(x)
    return derivada.subs(x, ponto).evalf(casas_decimais)


def funcao_no_ponto(y, ponto, casas_decimais):  # Resultado da função para um dado x
    return y.subs(x, ponto).evalf(casas_decimais)


def newton_raphson(y, chute, epsilon, casas_decimais):  # Metodo de Newton Raphson
    for count in range(1, 20):          # Adimite 20 iterações
        resultado_chute = funcao_no_ponto(y, chute, casas_decimais) # Retorna o resultado de f(x)
        resultado_derivada_no_ponto = derivada_funcao_no_ponto(y, chute, casas_decimais)    # Retorna o resultado de f'(x)

        novo_chute = N(chute - resultado_chute/resultado_derivada_no_ponto, casas_decimais)    # Calculo de Xcount+1 com base nos resultados

        if count == 1:
            x0 = chute
                                                                            # utilizando Xcount.
        resultado_novo_chute = funcao_no_ponto(y, novo_chute, casas_decimais)               # Calculo de Xcount+2 com base no resultado utilizando xk+1
        
        # Demonstra o resultado obtido na "count" iteração
        print("Tentativa {}: x = {}, f(x) = {}, f`(x) = {}".format(count, novo_chute, resultado_novo_chute, resultado_derivada_no_ponto))
            
        if abs(novo_chute - chute) < epsilon or abs(resultado_novo_chute) < epsilon:    # Checa as condições de parada.
            print("Erro Absoluto: {}".format(erro_absoluto(x0, chute, casas_decimais)))            
            return novo_chute                                                           # Se for atendida qualquer condição retorna o valor de Xcount+2
        chute = novo_chute                                                              # Caso não seja satisfeita nenhuma condição, atualiza
                                                                                        # o valor do novo chute para a pŕóxima iteração
    return 'Incapaz de calcular'                                                        # "Desiste" ao superar o limite máximo de iterações.


def newton_raphson_modificado(y, chute, epsilon, casas_decimais):
    resultado_derivada_no_ponto = derivada_funcao_no_ponto(y, chute, casas_decimais)
    for count in range(1, 20):
        resultado_chute = funcao_no_ponto(y, chute, casas_decimais)

        novo_chute = N(chute - resultado_chute/resultado_derivada_no_ponto, casas_decimais)

        if count == 1:
            x0 = chute

        resultado_novo_chute = funcao_no_ponto(y, novo_chute, casas_decimais)
        print("Tentativa {}: x = {}, f(x) = {}, f`(x) = {}".format(
            count, novo_chute, resultado_novo_chute, resultado_derivada_no_ponto))
        if abs(novo_chute - chute) < epsilon or abs(resultado_novo_chute) < epsilon:
            print("Erro Absoluto: {}".format(erro_absoluto(x0, chute, casas_decimais)))
            return novo_chute
        chute = novo_chute

    return 'Incapaz de calcular'

def posicao_falsa(y, intervalo, epsilon, casas_decimais):
    for count in range(1, 20):
        novo = (intervalo[1]*funcao_no_ponto(y, intervalo[0], casas_decimais) - intervalo[0]*funcao_no_ponto(y, intervalo[1], casas_decimais)) / (funcao_no_ponto(y, intervalo[0], casas_decimais) - funcao_no_ponto(y, intervalo[1], casas_decimais))

        if count == 1:
            x0 = novo

        resultado_funcao = funcao_no_ponto(y, novo, casas_decimais)
        print("Tentativa {}: a = {}, b = {}, x = {}, f(x) = {}".format(
            count, intervalo[0], intervalo[1], novo, resultado_funcao))
        if abs(resultado_funcao) < epsilon or abs(intervalo[0] - intervalo[1]) < epsilon:
            print("Erro Absoluto: {}".format(erro_absoluto(x0, novo, casas_decimais)))
            return novo
        intervalo = novo_intervalo(y, intervalo, novo)

    return 'Incapaz de calcular'

def isolamento(y, intervalo_isolamento):
    intervalos = []

    for i in range(intervalo_isolamento[0], intervalo_isolamento[1]+1):
        if funcao_no_ponto(y, i, casas_decimais).is_real and funcao_no_ponto(y, i+1, casas_decimais).is_real:
            if funcao_no_ponto(y, i, casas_decimais) * funcao_no_ponto(y, i+1, casas_decimais) < 0:
                intervalos.append((i, i+1))

    return intervalos # Retorna uma lista de tuplas, onde cada tupla indica um intervalo


def erro_absoluto(original, estimado, casas_decimais):
    ea = N((original - estimado) / estimado, casas_decimais)
    return abs(ea)


if __name__ == '__main__':
    a = 1
    x = Symbol('x')
    casas_decimais = 5
    epsilon = 0.00001
    intervalo_isolamento = (-100, 100) # O intervalo do eixo X que será verificado
    
    n = int(input("Digite o número de foguetes: "))

    for i in range(1, n+1):
        a = int(input("\nDigite o valor da constante 'a' do foguete {}: ".format(i)))

        # Função da questão
        y = a*x - x*ln(x)
        intervalos = isolamento(y, intervalo_isolamento)

        if len(intervalos):
            for j in range(len(intervalos)):
                print("\nPara o intervalo {}:".format(intervalos[j]))

                intervalo = intervalos[j]
                chute = (intervalo[0]+intervalo[1])/2

                print("\nMétodo do Posição Falsa:")
                try:
                    print("Resultado de 'd': {}".format(posicao_falsa(y, intervalo, epsilon, casas_decimais)))
                except Exception:
                    print("Impossível calcular")

                print("="*80)

                print("\nMétodo de Newton-Raphson:")
                try:
                    print("Resultado de 'd': {}".format(newton_raphson(y, chute, epsilon, casas_decimais)))
                except Exception:
                    print("Impossível calcular")
                print("="*80)

                print("\nMétodo de Newton-Raphson-Modificado:")
                try:
                    print("Resultado de 'd': {}".format(newton_raphson_modificado(y, chute, epsilon, casas_decimais)))
                except Exception:
                    print("Impossível calcular")

        else:
            print("Para a = {}, não existem raízes reais".format(a))
