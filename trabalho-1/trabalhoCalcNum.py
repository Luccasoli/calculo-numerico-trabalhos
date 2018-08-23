from math import log

def posicaoFalsa(a,d,e):
    pass 

def newtonRaphson(a,d,e):
    pass 

def newtonRaphsonModificado(a,d,e):
    pass 

if __name__ == '__main__':
    a = float(input("Digite o valor de a:"))
    d = float(input("Digite o valor de d:"))
    e = float(input("Digite o valor de ε:"))

    func = a*d - d*log(d)

    print("{:.2f}".format(func))