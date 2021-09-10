

host = input('Informe o HOST destino: ')
port = input('Informe a Porta que deseja analisar: '

nm = nmap.PortScanner()
nm.scan(hosts=host , ports=port)

print('#' *60)
print(nm)
print('-' *30)
print(dir(nm))
print('#' *60)


