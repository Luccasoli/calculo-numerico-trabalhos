# -*- coding: utf-8 -*-
from sympy import *


def novo_intervalo(y, intervalo, x3):
    y1 = y.subs(x, intervalo[0]).evalf()
    y2 = y.subs(x, intervalo[1]).evalf()
    y3 = y.subs(x, x3).evalf()

    if (y1 * y3 < 0):
        return [intervalo[0], x3]
    return [intervalo[1], x3]


def derivada_funcao_no_ponto(y, ponto):
    derivada = y.diff(x)
    return derivada.subs(x, ponto).evalf()


def funcao_no_ponto(y, ponto):  # Resultado da função para um dado x
    return y.subs(x, ponto).evalf()


def newton_raphson(y, chute, epsilon):  # Metodo de Newton Raphson
    for count in range(1, 20):          # Adimite 20 iterações
        resultado_chute = funcao_no_ponto(y, chute) # Retorna o resultado de f(x)
        resultado_derivada_no_ponto = derivada_funcao_no_ponto(y, chute)    # Retorna o resultado de f'(x)

        novo_chute = chute - resultado_chute/resultado_derivada_no_ponto    # Calculo de Xcount+1 com base nos resultados
                                                                            # utilizando Xcount.
        resultado_novo_chute = funcao_no_ponto(y, novo_chute)               # Calculo de Xcount+2 com base no resultado utilizando xk+1
        print("Tentativa {}: x = {}, f(x) = {}".format(                     # Demonstra o resultado obtido na "count" iteração
            count, novo_chute, resultado_novo_chute))
        if abs(novo_chute - chute) < epsilon or abs(resultado_novo_chute) < epsilon:    # Checa as condições de parada.
            return novo_chute                                                           # Se for atendida qualquer condição retorna o valor de Xcount+2
        chute = novo_chute                                                              # Caso não seja satisfeita nenhuma condição, atualiza
                                                                                        # o valor do novo chute para a pŕóxima iteração
    return 'Incapaz de calcular'                                                        # "Desiste" ao superar o limite máximo de iterações.


def posicao_falsa(y, intervalo, epsilon):
    for count in range(1, 20):
        novo = (intervalo[1]*funcao_no_ponto(y, intervalo[0]) - intervalo[0]*funcao_no_ponto(
            y, intervalo[1])) / (funcao_no_ponto(y, intervalo[0]) - funcao_no_ponto(y, intervalo[1]))

        resultado_funcao = funcao_no_ponto(y, novo)
        print("Tentativa {}: a = {}, b = {}, x = {}, f(x) = {}".format(
            count, intervalo[0], intervalo[1], novo, resultado_funcao))
        if abs(resultado_funcao) < epsilon or abs(intervalo[0] - intervalo[1]) < epsilon:
            return novo
        intervalo = novo_intervalo(y, intervalo, novo)

    return 'Incapaz de calcular'


if __name__ == '__main__':
    a = 1
    x = Symbol('x')
    casas_decimais = 5
    epsilon = 0.00001
    chute = 2.5
    intervalo = [2, 3]

    n = int(input("Digite o número de foguetes: "))

    for i in range(1, n+1):
        a = int(input("\nDigite o valor da constante 'a' do foguete {}: ".format(i)))

        # Função da questão
        y = a*x - x*log(x)

        print("Método do Ponto Falso:")
        try:
            print("Resultado de 'd': {}".format(posicao_falsa(y, intervalo, epsilon)))
        except Exception:
            print("Impossível calcular")

        print("="*100)

        print("Método de Newton-Raphson:")
        try:
            print("Resultado de 'd': {}".format(newton_raphson(y, chute, epsilon)))
        except Exception:
            print("Impossível calcular")
