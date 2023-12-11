from domain.book import Book


class BookInMemoryRepository:

    def __init__(self):
        """
        initializeaza lista de carti
        """

        self.__book_list = []

    def store(self, book: Book):
        """
        adauga o carte in lista de carti
        :param book: cartea de adaugat
        :raises ValueError: daca exista deja o carte cu acelasi id
        """

        if self.find(book.get_id()):
            raise ValueError("Exista deja o carte cu acest id!")
        self.__book_list.append(book)

    def find(self, id):
        """
        cauta o carte dupa id
        :param id: id-ul cartii de cautat
        :return: cartea cu id-ul dat sau None daca nu exista
        """

        for book in self.__book_list:
            if book.get_id() == id:
                return book
        return None

    def update(self, id, new_book):
        """
        modifica o carte
        :param id: id-ul cartii de modificat
        :param new_book: noua carte
        :raises ValueError: daca nu exista o carte cu id-ul dat
        """

        book_to_update = self.find(id)
        if book_to_update is None:
            raise ValueError("Nu exista o carte cu acest id!")
        self.__book_list[self.__book_list.index(book_to_update)] = new_book

    def delete(self, id):
        """
        sterge o carte
        :param id: id-ul cartii de sters
        :raises ValueError: daca nu exista o carte cu id-ul dat
        :return: cartea stearsa (pentru afisare)
        """

        book_to_delete = self.find(id)
        if book_to_delete is None:
            raise ValueError("Nu exista o carte cu acest id!")
        self.__book_list.remove(book_to_delete)
        return book_to_delete

    def get_current_list(self):
        """
        getter pentru lista de carti
        """

        return self.__book_list

    def size(self):
        """
        getter pentru lungimea listei de carti
        """

        return len(self.__book_list)

    def delete_all_books(self):
        for i in range(0, len(self.get_current_list())):
            self.delete(i)
