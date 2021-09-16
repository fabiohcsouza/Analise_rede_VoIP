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

ping_subprocess("192.168.1.1")