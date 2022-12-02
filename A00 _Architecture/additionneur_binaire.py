# Créé par Elève, le 15/09/2022 en Python 3.7

import psutil

battery = psutil.sensors_battery()
print(battery)


core = psutil.cpu_count()
print("Nombre de core :",core)