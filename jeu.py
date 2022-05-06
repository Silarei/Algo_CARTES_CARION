class Carte :
    def __init__ (self, mana, nom, description) :
        self._mana = mana
        self._nom = nom
        self._description = description

    def getMana (self) :
        return self._mana

    def setMana (self, new) :
        self._mana = new

    def getNom (self) :
        return self._nom

    def setNom (self, new) :
        self._nom = new

    def getDescription (self) :
        return self._description

    def setDescription (self, new) :
        self._description = new

class Crystal(Carte) :
    def __init__ (self, mana, nom, description, valeur) :
        super().__init__ (mana, nom, description)
        self._valeur = valeur

    def getValeur (self) :
        return self._valeur

    def setValeur (self, new) :
        self._valeur = new

class Creature(Carte) :
    def __init__ (self, mana, nom, description, pv, attackScore) :
        super().__init__(mana, nom, description)
        self._pv = pv
        self._attackScore = attackScore

    def getPv (self) :
        return self._pv

    def setPv (self, new) :
        self._pv = new

    def getAttackScore (self) : 
        return self._attackScore

    def setAttackScore (self, new) :
        self._attackScore = new

class Blast(Carte) :
    def __init__ (self, mana, nom, description, valeur) :
        super().__init__(mana, nom, description)
        self._valeur = valeur

    def getValeur (self) :
        return self._valeur

    def setValeur (self, new) :
        self._valeur = new

class Mage :
    def __init__ (self, nom, pv, manaTotal, main, defausse, zoneJeu) :
        self._nom = nom
        self._pv = pv
        self._manaTotal = manaTotal
        self._manaActuel = manaTotal
        self._main = main
        self._defausse = defausse
        self._zoneJeu = zoneJeu

    def getNom (self) :
        return self._nom

    def setNom (self, new) :
        self._nom = new

    def getPv (self) :
        return self._pv

    def setPv (self, new) :
        self._pv = new

    def getManaActuel (self) :
        return self._manaActuel
    
    def printManaActuel (self) :
        print(self._manaActuel)

    def setManaActuel (self, new) :
        self._manaActuel = new

    def getManaTotal (self) :
        return self._manaTotal

    def printManaTotal (self) :
        print(self._manaTotal)

    def setManaTotal (self, new) :
        self._manaTotal = new

    def printZoneJeu (self) :
        rep = ""
        for x in self._zoneJeu :
            rep = rep + x.getNom() + "; "
        return rep

    def jouerCarte (self, numCarte, cible) :
        if self._main[numCarte].getMana() <= self.getManaActuel() :
            self.setManaActuel(self.getManaActuel() - self._main[numCarte].getMana())
            if type(self._main[numCarte]) == Crystal :
                self.setManaTotal(self.getManaTotal() + self._main[numCarte].getValeur())
            if type(self._main[numCarte]) == Blast :
                cible.setPv(cible.getPv() - self._main[numCarte].getValeur())
                self._defausse.append(self._main[numCarte])
            else :
                self._zoneJeu.append(self._main[numCarte])
            self._main.pop(numCarte)
        else :
            print ("Pas assez de mana !")

    def regenMana (self) :
        self.setManaActuel(self.getManaTotal())

    def attack (self, attaquant, cible) :
        if (type(attaquant) == Creature ) :
            if (type(cible) == Mage or type(cible) == Creature) :
                cible.setPv(cible.getPv() - attaquant.getAttackScore())
                if (type(cible) == Creature) :
                    attaquant.setPv(attaquant.getPv() - cible.getAttackScore())
            else :
                print("Cible invalide")
        else :
            print("Attaquant invalide")

    def checkVie (self) :
        for x in self._zoneJeu :
            if type(x) == Creature :
                if x.getPv() < 1 :
                    self._defausse.append(x)
                    self._zoneJeu.remove(x)

CreatureUn = Creature(2, "Goblin beurré", 'Un goblin particulièrement alcoolisé', 1, 2)
CrystalUn = Crystal(0, "Grenat", "Une petite pierre rouge", 1)
BlastUn = Blast(3, "Jet de bouteille", "Lancez une bouteille sur un adversaire", 3)
JoueurUn = Mage("Bernard", 20, 3, [CreatureUn, CreatureUn, CrystalUn, BlastUn], [], [])
JoueurDeux = Mage("Michou", 20, 3, [CreatureUn, CreatureUn, CrystalUn, BlastUn], [], [])

print(JoueurUn.printZoneJeu())
JoueurUn.jouerCarte(1, JoueurDeux)
JoueurUn.printManaActuel()
print(JoueurUn.printZoneJeu())
JoueurDeux.jouerCarte(2, JoueurUn)
print(JoueurDeux.printZoneJeu())
print(JoueurDeux.printManaTotal())
JoueurDeux.jouerCarte(2, JoueurUn._zoneJeu[0])
print(JoueurDeux.printZoneJeu())
JoueurUn.checkVie()
print(JoueurUn.printZoneJeu())