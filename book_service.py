from domain.book import Book
from domain.validator import BookValidator
from repository.book_repository import BookInMemoryRepository
import random
import string


class BookController:
    def __init__(self, repository: BookInMemoryRepository, book_validator: BookValidator):
        """
        initializeaza controller-ul de carti
        :param repository: repository-ul de carti
        :param book_validator: validatorul de carti
        """

        self.__book_validator = book_validator
        self.__repository = repository

    def add_book(self, id, title, description, author, is_rented, no_rentals):
        """
        creeaza cartea book, o valideaza si o adauga in repository
        :param id: id-ul cartii
        :param title: titlul cartii
        :param description: descrierea cartii
        :param author: autorul cartii
        :param is_rented: statusul cartii
        :param no_rentals: numarul de inchirieri
        :raises ValueError: daca cartea nu este valida
        """

        book = Book(id, title, description, author, is_rented, no_rentals)
        self.__book_validator.validate_book(book)
        self.__repository.store(book)

    def delete_book(self, id):
        """
        sterge o carte
        :param id: id-ul cartii de sters
        :raises ValueError: daca nu exista o carte cu id-ul dat
        :return: cartea stearsa (pentru afisare)
        """

        return self.__repository.delete(id)

    def delete_all_books(self):
        """
        sterge toate cartile
        """

        for i in range(0,self.__repository.size()):
            self.__repository.delete(i)

    def update_book(self, id, title, description, author, is_rented, no_rentals):
        """
        modifica o carte
        :param id: id-ul cartii de modificat
        :param title: noul titlu al cartii
        :param description: noua descriere a cartii
        :param author: noul autor al cartii
        :param is_rented: noul status al cartii
        :param no_rentals: noul numar de inchirieri al cartii
        """

        new_book = Book(id, title, description, author, is_rented, no_rentals)
        self.__book_validator.validate_book(new_book)
        self.__repository.update(id, new_book)

    def get_all_books(self):
        """
        getter pentru lista de carti
        :return: lista de carti
        """

        return self.__repository.get_current_list()

    def filter_by_id(self, id):
        """
        :param id: id-ul cartii
        :return: cartea cu id-ul dat sau None daca nu exista
        """

        return [book for book in self.__repository.get_current_list() if book.get_id() == id]

    def filter_by_title(self, title):
        """
        :param title: titlul cartii
        :return: cartile cu titlul dat sau None daca nu exista
        """

        return [book for book in self.__repository.get_current_list() if book.get_title() == title]

    def find_book_by_id(self, book_id):
        """
        cauta o carte dupa id
        :param book_id: id-ul cartii
        :return: cartea cu id-ul dat sau None daca nu exista
        """
        
        for book in self.get_all_books():
            if book.get_id() == book_id:
                return book
        return None

    def generate_random_books(self, number):
        """
        genereaza number random carti
        :param number: numarul de carti de generat
        """

        for i in range(0, number):
            book_id = i
            book_title = ''.join(random.choices(string.ascii_lowercase, k=5))
            book_description = ''.join(random.choices(string.ascii_lowercase, k=5))
            book_author = ''.join(random.choices(string.ascii_lowercase, k=5))
            book_is_rented = random.choice(["rented", "available"])
            book_no_rentals = random.randint(0, number)
            book = Book(book_id, book_title, book_description, book_author, book_is_rented, book_no_rentals)
            self.__repository.store(book)



    def sort_by_number_of_books(self, report_list):
        """
        sorteaza raportul dupa numarul de carti inchiriate
        :param report_list: raportul generat
        :return: raportul sortat
        """

        b = 0
        while b == 0:
            b = 1
            for i in range(0, len(report_list) - 1):
                if report_list[i][0] > report_list[i + 1][0]:
                    aux = report_list[i]
                    report_list[i] = report_list[i + 1]
                    report_list[i + 1] = aux
                    b = 0
                elif report_list[i][0] == report_list[i + 1][0]:
                    if report_list[i][1].get_author() > report_list[i + 1][1].get_author():
                        aux = report_list[i]
                        report_list[i] = report_list[i + 1]
                        report_list[i + 1] = aux
                        b = 0
        return report_list
