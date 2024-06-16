RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carro_velocidade = 61
carro_local = 99


vel_carro_pass_radar_1 = carro_velocidade > RADAR_1
carro_passou_radar_1 = carro_local >= (LOCAL_1 - RADAR_RANGE) and carro_local <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro ultrapassou limite do radar 1')

if carro_passou_radar_1:
    print('Carro passou em radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')