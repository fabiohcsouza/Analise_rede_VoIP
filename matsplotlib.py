import os
import re
import numpy as np
import matplotlib.pyplot as mpl


ping = ["google.com.br", "8.8.8.8", "youtube.com"]

qnt_ping = 5
fs = np.linspace(1,qnt_ping,qnt_ping)

for p in ping:
   resp = os.system("ping {} {}".format(qnt_ping,p))
   #filtro = filter(lambda x: x[0].lower() in "time=(.*?) ms", str(resp))
   filtro = re.findall(str("time=(.*?) ms"),resp.read(),re.DOTALL)
   aping = np.array(filtro,np.float)
  # aping1 = np.array(qnt_ping)
   mpl.plot(fs,aping,"o-")

mpl.legend(ping)
mpl.show()