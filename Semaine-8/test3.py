class Citron:
    def __init__(self, masse=0):
        print("(2) J'arrive dans le .__init__()")
        self.masse = masse

    def get_masse(self):
        print("Coucou je suis dans le get")
        return self._masse

    def set_masse(self, valeur):
        print("Coucou je suis dans le set")
        if valeur < 0:
            raise ValueError("Un citron ne peut pas avoir"
                             " de masse négative !")
        self._masse = valeur

    masse = property(fget=get_masse, fset=set_masse)


if __name__ == "__main__":
     citron = Citron()
     citron.masse

