from domain.book import Book
from domain.client import Client
from domain.rentals import Rental
from domain.validator import BookValidator, ClientValidator


def test_create_book():
    """
    functie de test pentru crearea unui obiect de tip Book
    """

    book = Book(1, "titlu", "descriere", "autor", "available", 0,)
    assert book.get_id() == 1
    assert book.get_title() == "titlu"
    assert book.get_description() == "descriere"
    assert book.get_author() == "autor"
    assert book.get_is_rented() == "available"
    assert book.get_no_rentals() == 0


def test_create_client():
    """
    functie de test pentru crearea unui obiect de tip Client
    """

    client = Client(1, "nume", "5040422134154", 0)
    assert client.get_id() == 1
    assert client.get_name() == "nume"
    assert client.get_cnp() == "5040422134154"
    assert client.get_no_rentals() == 0


def test_create_rental():
    """
    functie de test pentru crearea unui obiect de tip Rental
    """

    client = Client(1, "nume", "5040422134154", 0)
    book = Book(1, "titlu", "descriere", "autor", "available", 0, )
    rental = Rental(client, book)
    assert rental.get_book() == book
    assert rental.get_client() == client


def test_validate_book():
    """
    functie de test pentru validarea unei carti
    """

    valid_book = Book(1, "abc", "abc", "abc", "rented", 0)
    invalid_book = Book(1, "", "", "", "", 0)
    book_validator = BookValidator()
    book_validator.validate_book(valid_book)

    try:
        book_validator.validate_book(invalid_book)
        assert False

    except ValueError:
        assert True


def test_validate_client():
    """
    functie de test pentru validarea unui client
    """

    valid_client = Client(1, "abc", "5040422134154", 0)
    invalid_client = Client(1, "", "", 0)
    client_validator = ClientValidator()
    client_validator.validate_client(valid_client)

    try:
        client_validator.validate_client(invalid_client)
        assert False

    except ValueError:
        assert True


def run_domain_tests():
    test_create_book()
    test_create_client()
    test_create_rental()
    test_validate_book()
    test_validate_client()
