# Equação do 2º:

def valores():
    print('ax² + bx + c\n')
    while True:
        try:
            a = int(input('Qual o valor de A?: '))
            if a == 0:
                print('A não pode ser 0 na equação de Segundo Grau')
                continue

            b = int(input('Qual o valor de B?: '))
            c = int(input('Qual o valor de C?: '))

        except ValueError:
            print('tente novamente!')
            continue
        return a, b, c


def calc_delta(abc):

    delta = abc[1]**2 - 4 * abc[0] * abc[2]
    if delta < 0:
        print('\n--- ATENÇÃO ---')
        print(f'A equação não possui valores Reais! Pois Delta < 0: {delta}\n')
    elif delta == 0:
        print('\n--- ATENÇÃO ---')
        print(f'A equação tem uma raiz real! pois Delta = 0\n')

    return delta


def calcular_x(abc, valor_delta):
    if valor_delta > 0:
        x1 = (-abc[1] + valor_delta**(1/2)) / (2 * abc[0])
        x2 = (-abc[1] - valor_delta**(1/2)) / (2 * abc[0])
        return x1, x2
    elif valor_delta == 0 and abc[1] == 0 and abc[2] == 0:
        x1 = (abc[0]**(1/2))
        return x1, 0
    elif valor_delta == 0:
        x = (-abc[1] / 2 * abc[0])
        return x, 0


def transformar(numero):
    if numero < 0:
        sinal = '-'
        return numero * -1, sinal
    else:
        sinal = '+'
        return numero, sinal


# Código Principal:
while True:
    resultado = valores()
    resultado_delta = calc_delta(resultado)
    if resultado_delta < 0:
        continue
    resultado_x = calcular_x(resultado, resultado_delta)
    print(resultado_x)

    print('\n--- Calculando ----')
    print(f'| Delta = {resultado[1]}² - 4 x {resultado[0]} x {resultado[2]}')
    print(f'| x1 = {-resultado[1]} + √{resultado_delta} / 2 x {resultado[0]}\n'
          f'| x2 = {-resultado[1]} - √{resultado_delta} / 2 x {resultado[0]}')

    print('\n---- Resultado ----')
    print(f' {transformar(resultado[0])[0]}x² {transformar(resultado[1])[1]} {transformar(resultado[1])[0]}x '
          f'{transformar(resultado[2])[1]} {transformar(resultado[2])[0]}')
    print('-' * 19)
    print(f'- Delta = {resultado_delta}\n- x1 = {resultado_x[0]:.2f}\n- x2 = {resultado_x[1]:.2f}\n' + '-' * 19 + '\n')
