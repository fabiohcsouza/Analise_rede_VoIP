def ping_subprocess(host):

    #Metodo de ping usando SOCKET:
    import subprocess
    import getpass

    usuario = getpass.getuser()

    local = r" >> C:\Users\{}\Desktop\LOG\test.txt".format(usuario)

    ping = subprocess.Popen(
        ["ping", "/l 160", "/n 30", {host}],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    out, error = ping.communicate()
    saida = out
    #print(saida)
    arquivo = open("log\ping\ping.", 'w')
    arquivo.write (f"{saida}")
    arquivo.close()

import os
import re
import numpy as np
import matplotlib.pyplot as mpl

ping = ["google.com.br", "8.8.8.8", "youtube.com"]

qnt_ping = 5
fs = np.linspace(1,qnt_ping,qnt_ping)

for p in ping:
    resp = os.popen("ping {}".format(p))
    resp_splip = resp.split
    qtd = len(resp_splip)
    filtro = (list(filter(lambda x: x[0].lower() in "time=(.*?) ms", str(resp_splip)),
    pin_s = np.array(filtro,np.float)
    mpl.plot (fs,pin_s,"o-")

mpl.legend(ping)
mpl.show()
