#Para una distribucion Poisson

lamda = 20
mu = 30
Q_servidores = 3

P = []
C = []

factor_de_uso = lamda/mu            #rho
L = lamda/(mu-lamda)                #cantidad esperada de clientes en el sistema
W = 1/(mu-lamda)                    #Tiempo esperado de uso
Wq = lamda/(mu*(mu-lamda))          #Tiempo esperado de espera en la cola
Lq = Wq * lamda                     #Cantidad esperada de clientes en la cola

# print(factor_de_uso, "\n", L, "\n", W, "\n", Wq, "\n", Lq, "\n", P0, "\n", P1, "\n", P2, "\n", P0+P1+P2)

P0 = 1-factor_de_uso
P.append(P0)

for i in range(1,40):              #sum(P) <= 1:
    Ultimo_P = P[-1]
    Nuevo_P = Ultimo_P * factor_de_uso
    P.append(Nuevo_P)

    # print("P sum: ",sum(P))

# print("P: ", P)
# print("P sum: ", sum(P))
for index, value in enumerate(P):
    print('Index:', index, ' Value: ', '{:f}'.format(value))

# P1 = P0 * factor_de_uso
# P2 = P1 * factor_de_uso