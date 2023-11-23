class Animal:
    def __init__(self,tip,putere,nume,picioare,nutritie):
        self.tip = tip
        self.putere = putere
        self.nume = nume
        self.picioare = picioare
        self.nutritie = nutritie

    def __str__(self):
        return f'Animalul este {self.tip}, numele sau este {self.nume}, are {self.picioare} picioare si are o nutritie {self.nutritie}'

    def __eq__(self, other):
        return self.tip== other.tip and self.nume == other.nume
    def creste_animal(self,up):
        for x in range (0,8):
            self.putere += up
            print(self.putere)
a = Animal("caine",200,"Azorel",4,"omnivor")
a.creste_animal(100)
print(a)

class Tip_Animal(Animal):
    def __init__(self, rasa,culoare):
        self.rasa = rasa
        self.culoare = culoare
    def __str__(self):
        return f'{self.tip} este un {self.rasa}, de culoarea {self.culoare}'
    def __eq__(self, other):
        return self.nume == other.nume and self.rasa == other.rasa and self.culoare == other.culoare

k = Tip_Animal("ciobanesc german","negru")
print(k)

class Stapan_Animal(Animal):
    def __init__(self,nume_stapan,CNP):
        self.nume_stapan = nume_stapan
        self.CNP  = CNP
    def __str__(self):
        return f'Numele stapanului {self.tip} este {self.nume_stapan}, are CNP-ul {self.CNP}'
    def __eq__(self, other):
        return self.CNP == other.CNP
proprietar = Stapan_Animal("Maria",000000)
print(proprietar)



