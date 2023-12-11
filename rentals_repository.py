from domain.rentals import Rental


class RentalInMemoryRepository:
    def __init__(self):
        """
        initializeaza lista de inchirieri
        """

        self.__rentals = []

    def store(self, rental: Rental):
        """
        adauga o inchiriere in lista de inchirieri
        :param rental: inchirierea de adaugat
        :raises ValueError: daca exista deja o inchiriere (o legatura intre client_id si book_id)
        """

        if self.find(rental.get_client().get_id(),rental.get_book().get_id()):
            raise ValueError("Exista deja aceasta inchiriere!")
        else:
            self.__rentals.append(rental)

    def delete(self, client_id, book_id):
        """
        sterge o inchiriere
        :param client_id: id-ul clientului
        :param book_id: id-ul cartii
        :raises ValueError: daca nu exista aceasta inchiriere
        """

        rental_to_delete = self.find(client_id, book_id)
        if rental_to_delete is None:
            raise ValueError("Nu exista aceasta inchiriere!")
        self.__rentals.remove(rental_to_delete)
        return rental_to_delete

    def find(self, client_id, book_id):
        """
        cauta o inchiriere dupa client_id si book_id
        :param client_id: id-ul clientului
        :param book_id: id-ul cartii
        :return: inchirierea cu client_id si book_id date sau None daca nu exista
        """

        for rental in self.__rentals:
            if rental.get_client().get_id() == client_id and rental.get_book().get_id() == book_id:
                return rental
        return None

    def get_current_list(self):
        """
        getter pentru lista de inchirieri
        """
        
        return self.__rentals

    def size(self):
        """
        getter pentru lungimea listei de inchirieri
        """

        return len(self.__rentals)
