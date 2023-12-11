from domain.rentals import Rental
from repository.rentals_repository import RentalInMemoryRepository
from service.client_service import ClientController
from service.book_service import BookController
from repository.book_repository import BookInMemoryRepository
from repository.client_repository import ClientInMemoryRepository
from domain.validator import ClientValidator
from domain.validator import BookValidator


class RentalController:
    def __init__(self, repository: RentalInMemoryRepository):
        """
        initializeaza controller-ul de inchirieri
        """

        self.__repository = repository

    def add_rental(self, client, book):
        """
        adauga o inchiriere in repository
        :param client: clientul care inchiriaza cartea
        :param book: cartea inchiriata
        """

        rental = Rental(client, book)
        self.__repository.store(rental)

    def delete_rental(self, client, book):
        """
        sterge o inchiriere din repository
        :param client: clientul care inchiriaza cartea
        :param book: cartea inchiriata
        """

        rental = Rental(client, book)
        self.__repository.delete(rental.get_client().get_id(), rental.get_book().get_id())

    def get_all_rentals(self):
        """
        getter pentru lista de inchirieri
        :return: lista de inchirieri
        """

        return self.__repository.get_current_list()

    def find_number_of_books_by_client(self, client_id):
        """
        calculeaza numarul de carti inchiriate de un client (la un moment anume)
        :param client_id: id-ul clientului
        :return: numarul de carti inchiriate de un client
        """
        
        p = 0
        for rental in self.__repository.get_current_list():
            if rental.get_client().get_id() == client_id:
                p = p + 1
        return p

    def find_number_of_rentals_by_book(self, book_id):
        """
        calculeaza numarul de inchirieri ale unei carti (la un moment anume)
        :param book_id: id-ul cartii
        :return: numarul de inchirieri ale unei carti
        """

        p = 0
        for rental in self.__repository.get_current_list():
            if rental.get_book().get_id() == book_id:
                p = p + 1
        return p
