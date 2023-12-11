class Book:
    def __init__(self, id, title, description, author, is_rented, no_rentals):
        """
        initializarea clasei Book
        :param int id: id-ul cartii
        :param string title: titlul cartii
        :param string description: descrierea cartii
        :param string author: autorul cartii
        :param string is_rented: statusul cartii
        :param int no_rentals: de cate ori a fost inchiriata cartea
        """
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__is_rented = is_rented
        self.__no_rentals = no_rentals

    def get_id(self):
        """
        getter pentru id-ul cartii
        :return int: id-ul cartii
        """

        return self.__id

    def get_title(self):
        """
        getter pentru titlul cartii
        :return string: titlul cartii
        """

        return self.__title

    def get_description(self):
        """
        getter pentru descrierea cartii
        :return string: descrierea cartii
        """

        return self.__description

    def get_author(self):
        """
        getter pentru autorul cartii
        :return string: autorul cartii
        """

        return self.__author

    def get_is_rented(self):
        """
        getter pentru statusul cartii
        :return string: statusul cartii
        """

        return self.__is_rented

    def get_no_rentals(self):
        """
        getter pentru numarul de inchirieri al cartii
        :return int: numarul de inchirieri al cartii
        """

        return self.__no_rentals

    def __str__(self):
        """
        transformarea obiectului de tip Book intr-un string
        :return string: cartea sub forma de string
        """

        return ("ID: " + str(self.get_id()) + " | " + "Titlu: " + self.get_title() + " | " + "Descriere: "
                + self.get_description() + " | " + "Autor: " + self.get_author() + " | " + " Disponibilitate: "
                + self.get_is_rented() + " | " + "Numar de inchirieri: "+ str(self.get_no_rentals()))
