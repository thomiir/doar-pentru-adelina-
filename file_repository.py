from repository.book_repository import BookInMemoryRepository
from repository.client_repository import ClientInMemoryRepository
from domain.book import Book
from domain.client import Client


class BookInFileRepository(BookInMemoryRepository):
    def __init__(self, fileN):
        BookInMemoryRepository.__init__(self)
        self.__fName = fileN
        self.__load_from_file()

    def __load_from_file(self):
        try:
            # f = open(self.__fName, "r")
            with open(self.__fName, "r") as f:
                line = f.readline().strip()
                while line != "":
                    attrs = line.split(",")
                    bk = Book(int(attrs[0]), attrs[1], attrs[2], attrs[3], attrs[4], 0)
                    BookInMemoryRepository.store(self, bk)
                    line = f.readline().strip()
                #f.close()

        except IOError:
            return

    def store(self, bk):
        BookInMemoryRepository.store(self, bk)
        self.__store_to_file()

    def update(self, id, bk):
        BookInMemoryRepository.update(self, id, bk)
        self.__store_to_file()

    def delete(self, id):
        book = BookInMemoryRepository.delete(self, id)
        self.__store_to_file()
        return book

    def __store_to_file(self):
        #f = open(self.__fName, "w")
        with open(self.__fName, "w") as f:
            bks = BookInMemoryRepository.get_current_list(self)
            for bk in bks:
                bkf = str(bk.get_id()) + "," + bk.get_title() + "," + bk.get_description() + "," + bk.get_author()
                bkf = bkf + "," + bk.get_is_rented() + "," + str(bk.get_no_rentals()) + "\n"
                f.write(bkf)
            #f.close()

    def removeAll(self):
        BookInMemoryRepository.delete_all_books(self)
        self.__store_to_file()


def test_book_CRUD():
    fileName = "testbook.txt"
    repo = BookInFileRepository(fileName)
    repo.removeAll()

    bk = Book(1, "tit", "des", "aut", "rented", 15)
    repo.store(bk)
    assert repo.size() == 1
    bk = Book(1, "titlu", "descriere", "autor", "rented", 15)
    repo.update(1, bk)
    assert repo.get_current_list()[0] == bk
    repo.delete(1)
    assert repo.size() == 0


class ClientInFileRepository(ClientInMemoryRepository):
    def __init__(self, fileN):
        ClientInMemoryRepository.__init__(self)
        self.__fName = fileN
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__fName, "r") as f:
                line = f.readline().strip()
                while line != "":
                    attrs = line.split(";")
                    cl = Client(int(attrs[0]), attrs[1], attrs[2], int(attrs[3]))
                    ClientInMemoryRepository.store(self, cl)
                    line = f.readline().strip()
                #f.close()

        except IOError:
            return

    def store(self, cl):
        ClientInMemoryRepository.store(self, cl)
        self.__store_to_file()

    def update(self, id, cl):
        ClientInMemoryRepository.update(self, id, cl)
        self.__store_to_file()

    def delete(self, id):
        client = ClientInMemoryRepository.delete(self, id)
        self.__store_to_file()
        return client

    def __store_to_file(self):
        #f = open(self.__fName, "w")
        with open(self.__fName, "w") as f:
            cls = ClientInMemoryRepository.get_current_list(self)
            for cl in cls:
                clf = str(cl.get_id()) + ";" + cl.get_name() + ";" + cl.get_cnp() + ";" + str(cl.get_no_rentals()) + "\n"
                f.write(clf)
            #f.close()

    def removeAll(self):
        ClientInMemoryRepository.delete_all_clients(self)
        self.__store_to_file()


def test_client_CRUD():
    fileName = "testclient.txt"
    repo = ClientInFileRepository(fileName)
    repo.removeAll()

    cl = Client(1, "nume", "5040422134154", 0)
    repo.store(cl)
    assert repo.size() == 1
    cl = Client(1, "nume2", "6040422134154", 15)
    repo.update(1, cl)
    assert repo.get_current_list()[0] == cl
    repo.delete(1)
    assert repo.size() == 0


test_book_CRUD()
test_client_CRUD()
