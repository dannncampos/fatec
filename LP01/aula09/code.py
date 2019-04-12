from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def distancia(self, pt):
        ### calcula a distância entre pt e o ponto atual ###
        dx = self.x - pt.x
        dy = self.y - pt.y
        dx = pow(dx, 2)
        dy = pow(dy, 2)
        d = sqrt(dx + dy)
        return d

class Poligono:
    pontos = []

    def add(self, pt):
        ### adiciona o ponto no polígono ###
        self.pontos.append(pt)

    def print(self):
        temp = ""
        for pt in self.pontos:
            if temp != "":
                temp = temp + pt.toString()
            else:
                temp = pt.toString()
        print( temp )

    def perimeter(self):
        """ calcula o perímetro do polígono """
        d = 0
        if len(self.pontos) > 1:
            ultimoPt = self.pontos[0]
            for pt in self.pontos:
                d += pt.distancia(ultimoPt)
                ultimoPt = pt
        return d

    def bbox(self):
        #verifica se existe pelo menos 1 ponto
        if len(self.pontos) > 0:
            #inicializa os valores com o 1o ponto
            xmin = self.pontos[0].x
            ymin = self.pontos[0].y
            xmax = self.pontos[0].x
            ymax = self.pontos[0].y
            #procura os valores na lista
            for pt in self.pontos:
                if pt.x < xmin:
                    xmin = pt.x
                if pt.y < ymin:
                    ymin = pt.y
                if pt.x > xmax:
                    xmax = pt.x
                if pt.y > ymax:
                    ymax = pt.y
            lowerLeft = Ponto(xmin, ymin)
            upperRight = Ponto(xmax, ymax)
            return Retangulo(lowerLeft, upperRight)
        else:
            return None

    def centroid(self):
        """ calcula o centroid do polígono """
        retangulo = self.bbox()
        if retangulo != None:
            return retangulo.centroid()
        else:
            return None


class Retangulo:
    def __init__(self, lowerLeft, upperRight):
        self.lowerLeft = lowerLeft
        self.upperRight = upperRight

    def centroid(self):
        x = self.upperRight.x - self.lowerLeft.x
        y = self.upperRight.y - self.lowerLeft.y
        return Ponto(x,y)

    def toPoligono(self):
        # adiciona os pontos no poligono
        inferiorEsquerdo = Ponto(self.lowerLeft.x, self.lowerLeft.y)
        inferiorDireito = Ponto(self.upperRight.x, self.lowerLeft.y)
        superiorDireito = Ponto(self.upperRight.x, self.upperRight.y)
        superiorEsquerdo = Ponto(self.lowerLeft.x, self.upperRight.y)
        poligono = Poligono()  # cria um novo polígono
        # coloca os 5 pontos do poligono, pois o 1o ponto precisa ser igual ao último
        poligono.add(inferiorEsquerdo)
        poligono.add(inferiorDireito)
        poligono.add(superiorDireito)
        poligono.add(superiorEsquerdo)
        poligono.add(inferiorEsquerdo)
        return poligono

    def print(self):
        print(self.lowerLeft.toString() +","+ self.upperRight.toString() )

class Linha:
    pontos = []

    def add(self, pt):
        ### adiciona o ponto na linha ###
        self.pontos.append(pt)

    def print(self):
        temp = ""
        for pt in self.pontos:
            if temp != "":
                temp = temp + pt.toString()
            else:
                temp = pt.toString()
        print( temp )

    def length(self):
        """ calcula o comprimento da linha """
        d = 0
        if len(self.pontos) > 1:
            ultimoPt = self.pontos[0]
            for pt in self.pontos:
                d += pt.distancia(ultimoPt)
                ultimoPt = pt
        return d
