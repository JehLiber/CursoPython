# Formatação de strings com método format

a = 'A'
b = 'B'
c = 1.1


# string = 'a={} b={} c={:.2f}'        -> OUTROS TIPOS
# formato = string.format(a, b, c)     -> OUTROS TIPOS

string = 'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)