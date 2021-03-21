# Defina una clase con variables para **name** y **country**.
# Luego defina un método que pertenece a la clase. El método 
# propósito es imprimir una frase que usa las variables.

# COMMIT INICIAL
# 2do commit: Se añadio comentario 2
# 3er commit: Se añadio comentario 3
# 4to commit: Se añadio comentario 4
# 5to commit: Se añadio comentario 5

class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def MyLocation (self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# Primera instancia de la clase Location
loc1 = Location("Tomas", "Portugal")
# Llamar a un método de la clase instanciada
loc1.MyLocation()

# Tres instancias más y llamadas a métodos para la clase Location
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.MyLocation()
loc3.MyLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.MyLocation ()
