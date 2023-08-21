def vogais(*args):
    vogais = 'aeiouAEIOU'
    count = 0 
    for e in args:
        for char in e:
            if char in vogais:
                count += 1
    return count
strings = str(input('Digite uma lista de strings separadas por espaço: ')).split()
print(f'Total de vogais:{vogais(*strings)}')