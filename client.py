class Client:
    def __init__(self, id, name, cnp, no_rentals):
        """
        initializarea clasei Client
        :param int id: id-ul clientului
        :param string name: numele clientului
        :param string cnp: cnp-ul clientului
        :param int no_rentals: cate carti a inchiriat clientul de-a lungul timpului
        """

        self.__id = id
        self.__name = name
        self.__cnp = cnp
        self.__no_rentals = no_rentals

    def get_id(self):
        """
        getter pentru id-ul clientului
        :return int: id-ul clientului
        """

        return  self.__id

    def get_name(self):
        """
        getter pentru numele clientului
        :return string: numele clientului
        """

        return self.__name

    def get_cnp(self):
        """
        getter pentru cnp-ul clientului
        :return string: cnp-ul clientului
        """

        return self.__cnp

    def get_no_rentals(self):
        """
        getter pentru cate carti a inchiriat clientul de-a lungul timpului
        :return int: cate carti a inchiriat clientul de-a lungul timpului
        """

        return self.__no_rentals

    def __str__(self):
        """
        transformarea obiectului de tip Client intr-un string
        :return string: clientul sub forma de string
        """

        return "ID: " + str(self.get_id()) + " | " + "Nume: " + self.get_name() + " | " + "CNP: " + self.get_cnp() + " | " + "Numar de carti inchiriate: " + str(self.get_no_rentals())