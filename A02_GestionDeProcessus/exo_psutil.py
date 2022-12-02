# Créé par Elève, le 06/10/2022 en Python 3.7

import psutil

"""
while True:
    temp = psutil.cpu_times()

    s = temp[0]
    m,s = s//60 , s%60
    h,m = m//60 , m%60

    print(f"{int(h)}h{int(m)}:{int(s)}")
"""

pid = psutil.pids()
print(pid)