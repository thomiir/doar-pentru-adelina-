from domain.book import Book
from domain.client import Client
from domain.validator import BookValidator
from repository.book_repository import BookInMemoryRepository
from service.book_service import BookController
from domain.validator import ClientValidator
from repository.client_repository import ClientInMemoryRepository
from service.client_service import ClientController
from repository.rentals_repository import RentalInMemoryRepository
from service.rentals_service import RentalController


def test_find_book_by_id():
    """
    functie de test pentru functia find_book_by_id()
    """

    repo = BookInMemoryRepository()
    validator = BookValidator()
    book_service = BookController(repo, validator)
    book_service.add_book(1, "titlu1", "descriere1", "autor1", "available", 0)
    book_service.add_book(2, "titlu2", "descriere2", "autor2", "available", 0)
    assert book_service.find_book_by_id(3) is None
    assert book_service.find_book_by_id(2) == book_service.get_all_books()[1]
    assert book_service.find_book_by_id(1) == book_service.get_all_books()[0]


def test_filter_books_by_title():
    """
    functie de test pentru functia filter_books_by_title()
    """

    repo = BookInMemoryRepository()
    validator = BookValidator()
    book_service = BookController(repo, validator)
    book_service.add_book(1, "titlu1", "descriere1", "autor1", "available", 0)
    book_service.add_book(2, "titlu2", "descriere2", "autor2", "available", 0)
    result = book_service.filter_by_title("titlu1")
    assert result == [book_service.get_all_books()[0]]

    book_service.add_book(3, "titlu2", "descriere2", "autor2", "available", 0)
    result = book_service.filter_by_title("titlu2")
    assert result == [book_service.get_all_books()[1],book_service.get_all_books()[2]]


def test_filter_books_by_id():
    """
    functia de test pentru functia filter_books_by_id()
    """

    repo = BookInMemoryRepository()
    validator = BookValidator()
    book_service = BookController(repo, validator)
    book_service.add_book(1, "titlu1", "descriere1", "autor1", "available", 0)
    book_service.add_book(2, "titlu2", "descriere2", "autor2", "available", 0)
    result = book_service.filter_by_id(1)
    assert result == [book_service.get_all_books()[0]]

    result = book_service.filter_by_title(3)
    assert result == []


def test_find_client_by_id():
    """
    functie de test pentru functia find_client_by_id()
    """

    repo = ClientInMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    client_service.add_client(1, "nume1", "5040422134154", 0)
    client_service.add_client(2, "nume2", "6040422134154", 0)
    assert client_service.find_client_by_id(3) is None
    assert client_service.find_client_by_id(2) == client_service.get_all_clients()[1]
    assert client_service.find_client_by_id(1) == client_service.get_all_clients()[0]



def test_filter_clients_by_name():
    """
    functie de test pentru functia filter_by_name()
    """

    repo = ClientInMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    client_service.add_client(1, "nume1", "5040422134154", 0)
    client_service.add_client(2, "nume2", "6040422134154", 0)
    result = client_service.filter_by_name("nume1")
    assert result == [client_service.get_all_clients()[0]]

    result = client_service.filter_by_id("nume3")
    assert result == []


def test_filter_clients_by_id():
    """
    functie de test pentru functia filter_by_id()
    """

    repo = ClientInMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    client_service.add_client(1, "nume1", "5040422134154", 0)
    client_service.add_client(2, "nume2", "6040422134154", 0)
    result = client_service.filter_by_id(1)
    assert result == [client_service.get_all_clients()[0]]

    result = client_service.filter_by_id(3)
    assert result == []


def test_find_number_of_books_by_client():
    """
    functie de test pentru functia find_number_of_books_by_client()
    """

    repo = RentalInMemoryRepository()
    rental_service = RentalController(repo)
    client1 = Client(1, "nume1", "5040422134154", 0)
    book1 = Book(1, "titlu1", "descriere1", "autor1", "available", 0)
    book2 = Book(2, "titlu2", "descriere2", "autor2", "available", 0)
    rental_service.add_rental(client1, book1)
    rental_service.add_rental(client1, book2)
    assert rental_service.find_number_of_books_by_client(client1.get_id()) == 2


def test_find_number_of_rentals_by_book():
    """
    functie de test pentru functia find_number_of_rentals_by_book()
    """

    repo = RentalInMemoryRepository()
    rental_service = RentalController(repo)
    client1 = Client(1, "nume1", "5040422134154", 0)
    book1 = Book(1, "titlu1", "descriere1", "autor1", "available", 0)
    rental_service.add_rental(client1, book1)
    assert rental_service.find_number_of_rentals_by_book(book1.get_id()) == 1


def run_service_tests():
    test_find_book_by_id()
    test_filter_books_by_title()
    test_filter_books_by_id()
    test_find_client_by_id()
    test_filter_clients_by_name()
    test_filter_clients_by_id()
    test_find_number_of_books_by_client()
    test_find_number_of_rentals_by_book()
