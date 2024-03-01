"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

range_menor = (LOCAL_1 - RADAR_RANGE)
range_maior = (LOCAL_1 + RADAR_RANGE)
carro_passou_radar = local_carro >= range_menor and local_carro <= range_maior



if carro_passou_radar:
    if velocidade > RADAR_1:
        print('MULTADO!')
    else:
        print('SEM MULTA')
else:
    print('SEM REGISTRO')
