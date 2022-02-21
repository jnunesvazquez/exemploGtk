"""
.. module::obxectos
    :platform: Unix, Windows
    :synopsis: Exemplos das clases en python
.. moduleauthor:: Braiskiskos <bmartinezparedes@gmail.com>
"""
class Punto:
    """
    Clase que define a un punto en un plano de duas dimensions
    Exemplo de documentación segundo o PEP 257
    """

    def __init__(self, x=0, y=0):
        """
        Constructor que define las propiedades de x e y dun punto bidimensional.
        :param x: Coordenada x do punto
        :param y: Coordenada y do punto
        """
        self.x = x
        self.y = y


class Circulo(Punto):
    """
    Clase circulo que se crea a partir de la clase circulo.
    """
    def __init__(self, x, y, r):
        """
        Constructor que define las propiedades de x e y dun punto bidimensional a partir del cual se crea un
        circulo con un radio r.
        :param x: Coordenada x do punto eredados da superclase Punto
        :param y: Coordenada y do punto eredados da superclase Punto
        :param r: Tamaño del circulo
        """
        Punto.__init__(self, x, y)
        self.r = r


class Punto2:
    """
    Clase que define a un punto en un plano de duas dimensions
    """

    def __init__(self, x, y):
        """x e y estan ocultos
        Constructor que define las propiedades de x e y dun punto bidimensional.
        :param x: Coordenada x do punto
        :param y: Coordenada y do punto
        """

        self.__x = x
        self.__y = y

    def getX(self):
        """
        Metodo para retornar el parametro x
        :return: Valor de X
        """
        return self.__x

    def getY(self):
        """
        Metodo para retornar el parametro y
        :return: Valor de Y
        """
        return self.__y

    def setX(self, x):
        """
        Método que permite dar valor a coordenada x do punto.
        O método asigna o valor da coordenada x sempre que sexa x>0. En caso contrario
        lo inicializara en 0.
        :param x: Parametro a darlle valor no eixe da x
        """
        if x > 0:
            self.__x = x
        else:
            self.__x = 0
            print("Valor inicializado en 0")

    def setY(self, y):
        """
        Método que permite dar valor a coordenada y do punto.
        O método asigna o valor da coordenada x sempre que sexa y>0. En caso contrario
        lanza unha excepcion de tipo ValueError.
        :param y: Parametro a darlle valor no eixe da y
        :raises ValueError: Excepcion que nos dara se o valor é menor de 0
        """
        if y > 0:
            self.__y = y
        else:
            raise ValueError
            #self.__y = 0
            #print("Valor inicializado en 0")

    # Sirve para comparar este objeto con otro Ej p seria distinto a p2 por que las coordenadas no son iguales
    def __eq__(self, other):
        """
        Sirve para comparar este objeto con otro Ej p seria distinto a p2 por que las coordenadas no son iguales
        :param other: Objeto con el cual queremos compararlo
        :return: false o truen dependiendo si es igual o no
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    x = property (getX, setX)

    y = property (getY, setY)


p2 = Punto2(3, 5)
print(p2._Punto2__x)
# print(p2._Punto2__getY())

p = Punto(1, 3)
c = Circulo(2, 3, 6)
print(p.x)
print(c.x)
# Para asignarle valor a una variable privada/oculta
p2.__x = 10  # Esto no funciona
p2.x = 10  # Esto si

"""
Deriban de objet
__init__(self,args) Inicializa los valores
__new__(cls,args) Crea el objeto
__del__(self) Livera la memoria de ese objeto
__str__(self) Funciona como un toString
__eq__(self,outo) Para comparar objetos Hay que implementarlo
"""
print(p2.__eq__(p))
# print(p2==p)


#Excepciones
try:
    print(5/0)
except (ZeroDivisionError,SyntaxError):
    print("Erro: Non se pode hacer division por 0")
except ValueError:
    print("Erro: valor incorrecto")
else:
    print("A division realizouse")
finally:
    print("A division fixose ou non")




def unha_funcion(p1,p2):
    print(p1)
    print(p2)

unha_funcion("hola", 2.366)
unha_funcion(p2=2.366,p1="hola")
def unha_funcion2(p1="p1",p2=3.000):
    print(p1)
    print(p2)
unha_funcion2()
unha_funcion2(p1="KISKOS")

def suma(*n):
    suma= 0
    for numeros in n:
        suma =suma +numeros
    return suma
print(suma(1,2,3,4,5,6))
def suma2(n1,n2,**numeros):
    suma=n1+n2
    for n in numeros.items():
        suma=suma+n[1]
    return suma

print(suma2(1,2,numero3=3, numeros4=4))