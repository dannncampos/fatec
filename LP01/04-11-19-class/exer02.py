from 04-11-19-class.code import *

r = Retangulo(Ponto(1, 1), Ponto(3, 3))
r.print()
print(r.centroid().toString())
p = r.toPoligono()
p.print()

print("Perímetro: ", p.perimeter())
