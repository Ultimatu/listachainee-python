#creation de la class de Maillon servant à rélier les éléments de la liste 
class Maillon:
    """Celllule d'une liste chainée."""
    def __init__(self, valeur):
        self._valeur = valeur
        self.suivant = None


class Liste:
    """Implémentation d'une liste chaînée vide et usage des différentes functions."""

    def __init__(self):
        """
        Déclaration du contructeur de la liste chainée vide, elle est opérationnelle
        dès que l'on appel la Class Liste()
        """
        self.tete = None  # La tête de la liste
        self.fin = None  # La fin de la liste

    # Test si la liste chainée est vide
    def estVide(self):
        """
        Renvoie `Oui` si la liste chaînée est vide, renvoie `Non` sinon.
        : Mode d'usage: 
        >>> `liste = Liste()` 
        >>> `liste.estVide()`

        # Affiche: Oui car la liste est vide 

        """

        if self.tete == None:
            return "Oui"
        else:
            return "Non"


    # Affiche les éléments de la liste chainée
    def AfficheList(self):
        """
        Cette fonction parcourt la liste chaînée et affiche tous les éléments contenus dans la liste. Elle affiche également "None" à la fin pour indiquer la fin de la liste.
        : `Mode d'utilisation:`
        >>> `liste = Liste()`
        >>> `liste.ajouterEnTete(1)`
        >>> `liste.ajouterEnTete(2)`
        >>> `liste.ajouterEnFin(3)`
        >>> `liste.afficherListe()`

        # Affiche: 2 -> 1 -> 3 -> None
        """

        if self.tete is None:
            print("La liste est vide")
            return
        else:
            deb = self.tete
            while deb is not None:
                print(deb._valeur, end="->")
                deb = deb.suivant
                if deb is None:
                    print("None")


    #Afficher l'élément courant en tête de la liste
    def elementCourant(self):
        
        """
        Cette function retourne l'élément courant de la liste si elle n'est pas vide.
        : `Mode d'utilisation:`
        >>> `liste = Liste()`
        >>> `liste.ajouterEnTete(1)`
        >>> `liste.ajouterEnTete(2)`
        >>> `liste.ajouterEnFin(3)`
        >>> `liste.elementCourant()`

        # Affiche: 1

        """
        if self.tete is None:
            print("La liste est vide")
            return
        else:
            return self.tete._valeur
        
    # Renvoi La taille de la liste chainée
    def Taille(self):
        """
        Renvoie la taille de la liste chaînée.
        : Mode d'usage: 
        >>> `l1 = Liste()` 
        >>> `l1.AjouteTete(1)`
        >>> `l1.Taille()`

        # Affiche: 1 parcequ'on a insérer un seul élément
        """

        mail = self.tete
        i = 0
        while mail is not None:
            mail = mail.suivant
            i += 1
        return i


    #Rechercher le premier indice d'un élément de la liste

    def searchIndice(self, _item):
        """
        Renvoie le premier indice de l'élément `_item` donné.
        si le resultat est -1 cela signifie que l'élément n'est pas dans la liste.
        : Mode d'usage: 
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)`
        >>> `l1.searchIndice(1)` 

        # Affiche: 0
        """
        if self.tete == None:
            raise IndexError("La liste est vide")
        current = self.tete
        index = 0
        while current is not None:
            if current._valeur == _item:
                return index
            current = current.suivant
            index += 1
        return -1  # l'élément n'est pas dans la liste

        
    # Rechercher des indices d'un élément de la liste par sa valeur donnée
    def searchAllIndice(self, item):
        """
        Renvoie  tout les indices de l'élément  `item` donné.\n
        : Mode d'usage: 
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.searchAllIndice(2)`

        # Affiche: [1, 3] car la valeur 2 figure deux fois dans le tableau
        """
        i = 0
        index = []
        mail = self.tete
        while mail.suivant is not None:

            if mail._valeur == item:
                index.append(i)
            i += 1
            mail = mail.suivant
        return index
    

    #compter le nombre d'occurence d'une valeur
    def countValue(self, _item):
        """
        Cette function permet de compter le nombre d'occurence de la valeur donnée
        en paramètre.
        : Mode d'usage: 
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.countValue(2)`

        # Affiche: 2 car la valeur 2 figure deux fois dans le tableau
        """
        if self.tete is None:
            raise IndexError("La liste est vide")
        else:
            current = self.tete
            value = 0
            while current:
                if current._valeur == _item:
                    value += 1
                current = current.suivant
            return value


     # Rechercher un élément dans la liste par sa position
    def searchValeur(self, indice):
        """
        Renvoie  l'élément à  l'indice donné.\n
        : Mode d'usage: 
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.searchValeur(2)`

        # Affiche: 5 car 5 est à l'indice 2
        """
        if indice >= self.Taille():
            raise ValueError("L'indice donnée est superieur à la taille de la Liste")

        else:
            i = 0
            mail = self.tete
            while i < indice:
                i += 1
                mail = mail.suivant
        return mail._valeur


    # Ajouter un élément à la tête de la liste
    def AjoutTete(self, _item):
        """
            Ajoute un élément au début de la liste chaînée.\n
            Mode d'usage: \n
            >>> `l1 = Liste()` \n
            >>> `l1.AjoutTete(1)`\n
            >>> `l1.AfficheListe()`\n
            # Affiche: 1
        """

        mail_item = Maillon(_item)
        mail_item.suivant = self.tete
        self.tete = mail_item


    # Ajouter un élément à la fin de la liste
    def AjoutFin(self, _item):
        """
        Ajoute un élément à la fin de la liste chaînée.\n
        Mode d'usage: \n
        >>> `l1 = Liste()` \n
        >>> `l1.AjoutFin(1)`\n
        >>> `l1.AfficheListe()`\n
        # Affiche: 1
        """

        if self.tete == None:  # s'il n' y a aucun éléments en tête
            self.tete = Maillon(_item)
            self.fin = self.tete

        elif self.fin == self.tete:  # s'il y'a un seul élément dans la liste
            self.fin = Maillon(_item)
            self.tete.suivant = self.fin

        else:
            elemnt_courrant = Maillon(_item)
            self.fin.suivant = elemnt_courrant
            self.fin = elemnt_courrant


    # Ajouter un élément à une postion donnée de la liste
    def AjoutPos(self, position, _item):
        """
        Insère un élément à l'indice i.\n
        Mode d'usage: \n
        >>> `l1 = Liste()` \n
        >>> `l1 = AjoutTete(1)` \n
        >>> `l1 = AjoutFin(2)` \n
        >>> `l1 = AjoutFin(5)` \n
        >>> `l1 = AjoutFin(10)` \n
        >>> `l1.AjoutPos(3, 20)`\n
        >>> `l1.AfficheListe()`\n
        # Affiche: 1 -> 2-> 5 -> 20 -> 10 -> None
        """

        if position < 0:  # si l'indice donné est inférieur à 0
            raise IndexError("La position ne peut pas être inferieur à 0.")

        elif position > self.Taille():  # si l'indice donné est superieur à la Taille de la liste
            raise IndexError("La position est plus que la taille de liste.")

        else:
            i = 0
            mail = self.tete
            while i < (position - 1):
                i += 1
                mail = mail.suivant

            mail_element = Maillon(_item)
            mail_element.suivant = mail.suivant
            mail.suivant = mail_element


    def SupTete(self):
        """
        cette function permet supprime l'élémént en tête de la liste.
        """

        if self.tete is None:
            print("La liste est vide, il n'y a rien à supprimer.")
        else:
            if self.tete == self.fin:
                self.fin = None
            self.tete = self.tete.suivant


    # Supprimer l'élément à la fin de la liste 
    def SupFin(self):
        """
        Retire la dernière cellule de la liste chaînée.\n
        Mode d'usage:\n
        >>> `l1 = Liste()` \n
        >>> `l1 = AjoutTete(1)` \n
        >>> `l1 = AjoutFin(2)` \n
        >>> `l1 = AjoutFin(5)` \n
        >>> `l1 = AjoutFin(2)` \n
        >>> `l1.SupFin()`\n
        # Affiche: 1 -> 2 -> 5 -> None
        """

        if self.Taille() == 0:
            raise ValueError("La liste chaînée est vide.")

        elif self.Taille() == 1:
            self.tete = None
            self.fin = None

        else:  # Le pointeur s'arête sur le dernier éléments du tableau
            mail = self.tete
            # Le pointeur s'arête sur le dernier éléments du tableau
            while mail.suivant.suivant is not None: 
                mail = mail.suivant

            mail.suivant = None
            self.fin = mail

    #Supprimer toutes les valeurs  d'un élément donnée de la liste 
    def SupAllElement(self, _item):
        """Retire tous les éléments qui ont pour valeur l'_item donné."""

        if self.Taille() == 0:
            raise ValueError("La liste chaînée est vide.")

        mail = self.tete
        mail_courant = None
        while mail is not None:
            if mail._valeur == _item:

                #Si il n'y a qu'une seule mail dans la liste chaînée
                if self.tete == self.fin:
                    self.tete = None
                    self.fin = None

                #Si la mail à supprimer est la dernière
                elif mail == self.fin:
                    self.SupFin()

                #Si la mail à supprimer est la première
                elif mail == self.tete:
                    self.SupTete()

                else:
                    #La mail précédant est la mail à supprimer fait référence à la mail suivant la mail à supprimer
                    mail_courant.suivant = mail.suivant

            else:
                mail_courant = mail

            mail = mail.suivant
    #Effacer la prémière occurence de la valeur donnée dans la liste
    def supFirstValue(self, _item):
        """Retire la première occurence de  l'éléments l'_item donné 
        en faisant appel à la function SupPos(). Elle retourne -1 si l'élément ne 
        figure pas dans la liste
        :Mode d'usage
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.SupFirstValue(2)`
        >>> 'l1.AfficheList()

        # Affiche: 1 -> 5 -> 2 -> None
        """

        if self.tete == None:
            raise IndexError("La liste est vide")
        current = self.tete
        index = 0
        while current is not None:
            if current._valeur == _item:
                return self.SupPos(index)
            current = current.suivant
            index += 1
        return -1  # l'élément n'est pas dans la liste


    #Supprimer un élément donnée de la liste 
    def SupPos(self, postion):
        """
        Retire un élément à l'indice postion.
        :Mode d'usage
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.SupPos(2)`
        >>> 'l1.AfficheList()`

        # Affiche: 1 -> 2 -> 2 -> None

        """

        if postion < 0:
            raise IndexError("La position ne peut pas être inferieur à 0.")

        elif postion > self.Taille():
            raise IndexError("La position ne peut pas être superieur à la taille de liste.")

        elif postion == 0:
            self.SupTete()

        elif postion == self.Taille():
            self.SupFin()

        else:
            i = 0
            mail = self.tete
            mail_courant = None
            while i < postion:
                i += 1
                mail_courant = mail
                mail = mail.suivant

            mail_courant.suivant = mail.suivant
    

    #Fonction qui efface la liste entière
    def effaceListe(self):
        """
        Cette function parcour la liste et supprime chaque élément à l'aide de la
        function `SupTete()` et une fois la liste vide, elle fait appel à la function
        `AfficheList()`qui confirme que la liste est vide...
        :Mode d'usage
        >>> `l1 = Liste()` 
        >>> `l1 = AjoutTete(1)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1 = AjoutFin(5)` 
        >>> `l1 = AjoutFin(2)` 
        >>> `l1.effaceList()`

        # Affiche: La liste est vide.
        """
        
        mail = self.tete
        while mail is not None:
            self.SupTete()
            mail = mail.suivant
        return self.AfficheList()
            

#voilà comment calculer le temps d'éxecution d'une  function python.
#_____Premièrement: Importer le module time en faisant import time
#_______start_time = time.perf_counter()
#__________ma_function()
#_______end_time = time.perf_counter()
#_________print("Temps d'exécution :", end_time - start_time)

#___________EXEMPLE_AVEC_LA_FUNCTION__AjoutFin()___
#
#Déclarons une liste vide__
#___l1 = Liste()
#On débute le compteur__
#___temps_debut = time.perf_counter()
#__Insérons maintenant 10 élément dans la liste 
#for i in range(10):
#   l1.AjoutFin(10)
#
#on arrête le compteur
#temps_fin = time.perf_counter()
#Maintenant pour avoir le temps d'éxécution on fait  temps de fin moins temps_debut
#temps_execution = temps_fin - temps_debut
#print("Temps  d'éxectution =>", temps_execution)




