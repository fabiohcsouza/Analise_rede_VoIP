from io import DEFAULT_BUFFER_SIZE
import subprocess


#host = input('Informe o IP: ')

def ping_portal(host):

    timeout = '/n 4'
    size = '/l 160'

    # Abre um subprocess ping usando a sixtaxe Windows
    #p = cmd.run(['ping', host], stdout=subprocess.PIPE)

    # stdout = l.stdout
    #stdout = p.stdout

    
    # no windows
    #return stdout.decode('ISO-8859-1') if p.returncode == 0 else ''


    #recebe o valor

arquivoTemporario = tempfile.TemporaryFile()
arquivoTemporario.write(b'ping /n 30 /l 160 {} > ping_portal.txt'.format(entrada))
arquivoTemporario.seek(0)
print(str(arquivoTemporario.read(), encoding='utf8'))
arquivoTemporario.close()