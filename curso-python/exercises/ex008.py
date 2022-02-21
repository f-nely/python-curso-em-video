distancia = float(input('Digite uma distância em metros: '))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f'A medida de {distancia}m corresponde a \n {km}km \n {hm}hm \n '
      f'{dam}dam \n {dm}dm \n {cm}cm \n {mm}mm')
