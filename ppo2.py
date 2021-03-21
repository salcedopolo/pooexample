# Dado un valor de radio, imprima la circunferencia de un círculo.
# La fórmula para una circunferencia es c = pi * 2 * radio

class Circle:

    def __init__ (self, radio):
        self.radius = radio

    def circumference(self):
      pi = 3,14
      CircunferenceValue = pi * self.radius * 2
      return CircunferenceValue

    def printCircumference (self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

# Primera instancia de la clase Circle.
circle1 = Circle(2)
# Llame a la PrintCircumference para la clase circle1 instanciada.
circle1.printCircumference()

# Dos instancias más y llamadas a métodos para la clase Circle.
circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()
