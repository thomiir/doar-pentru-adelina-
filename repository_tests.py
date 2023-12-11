from domain.book import Book
from domain.client import Client
from domain.rentals import Rental
from repository.book_repository import BookInMemoryRepository
from repository.client_repository import ClientInMemoryRepository
from repository.rentals_repository import RentalInMemoryRepository


def test_CRUD_book_repository():
    """
    functie de test pentru repository-ul de carti
    """
    
    test_repository = BookInMemoryRepository()
    assert test_repository.size() == 0

    book1 = Book(1, "Titlul primei carti", "Descrierea primei carti", "Autorul primei carti", "available", 0)
    test_repository.store(book1)
    assert test_repository.size() == 1

    book2 = Book(1, "Titlu_nou", "Descriere_noua", "Autor_nou", "rented", 0)
    test_repository.update(1, book2)

    current_list = test_repository.get_current_list()
    assert current_list[0].get_title() == "Titlu_nou"
    assert current_list[0].get_description() == "Descriere_noua"
    assert current_list[0].get_author() == "Autor_nou"
    assert current_list[0].get_is_rented() == "rented"
    assert current_list[0].get_no_rentals() == 0

    try:
        test_repository.store(book1)
        assert False

    except ValueError:
        assert True

    test_repository.delete(book1.get_id())
    assert test_repository.size() == 0

    try:
        test_repository.delete(book1.get_id())
        assert False

    except ValueError:
        assert True


def test_CRUD_client_repository():
    """
    functie de test pentru repository-ul de clienti
    """

    test_repository = ClientInMemoryRepository()
    assert test_repository.size() == 0

    client1 = Client(1, "nume1", "5040422134154", 0)
    test_repository.store(client1)
    assert test_repository.size() == 1

    client2 = Client(1, "Nume_nou", "6040422134154", 0,)
    test_repository.update(1, client2)

    current_list = test_repository.get_current_list()
    assert current_list[0].get_name() == "Nume_nou"
    assert current_list[0].get_cnp() == "6040422134154"
    assert current_list[0].get_no_rentals() == 0

    try:
        test_repository.store(client1)
        assert False

    except ValueError:
        assert True

    test_repository.delete(client1.get_id())
    assert test_repository.size() == 0

    try:
        test_repository.delete(client1.get_id())
        assert False

    except ValueError:
        assert True


def test_CRUD_rentals_repository():
    """
    functie de test pentru repository-ul de inchirieri
    """

    test_repository = RentalInMemoryRepository()
    assert test_repository.size() == 0

    book = Book(1, "titlu", "desc", "autor","available", 0)
    client = Client(1,"nume", "5040422134154", 0)
    rental = Rental(client, book)
    test_repository.store(rental)
    assert test_repository.size() == 1

    try:
        test_repository.store(rental)
        assert False

    except ValueError:
        assert True

    test_repository.delete(rental.get_client().get_id(),rental.get_book().get_id())
    assert test_repository.size() == 0

    try:
        test_repository.delete(rental.get_client().get_id(),rental.get_book().get_id())
        assert False

    except ValueError:
        assert True


def run_repository_tests():
    test_CRUD_book_repository()
    test_CRUD_client_repository()