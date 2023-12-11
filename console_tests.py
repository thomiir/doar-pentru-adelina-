from ui.console import Console
from domain.book import Book
from domain.client import Client
from domain.rentals import Rental
from domain.validator import BookValidator, ClientValidator
from service.book_service import BookController
from service.client_service import ClientController
from service.rentals_service import RentalController
from repository.book_repository import BookInMemoryRepository
from repository.client_repository import ClientInMemoryRepository
from repository.rentals_repository import RentalInMemoryRepository


def test_most_rented_books():
    """
    functie de test pentru functia most_rented_books_report()
    """

    book_repo = BookInMemoryRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repo, book_validator)
    client_repo = ClientInMemoryRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repo, client_validator)
    rental_repo = RentalInMemoryRepository()
    rental_controller = RentalController(rental_repo)
    book1 = Book(1, "tit", "tit", "tit", "rented", 10)
    book2 = Book(2, "lop", "lop", "lop", "rented", 5)
    book_repo.store(book1)
    book_repo.store(book2)
    test_console = Console(book_controller, client_controller, rental_controller)
    report_list = test_console.most_rented_books_report_ui()

    assert report_list == [[10, book1], [5, book2]]


def test_most_active_clients():
    """
    functie de test pentru functia most_active_clients()
    """

    book_repo = BookInMemoryRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repo, book_validator)
    client_repo = ClientInMemoryRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repo, client_validator)
    rental_repo = RentalInMemoryRepository()
    rental_controller = RentalController(rental_repo)
    client1 = Client(1, "nume", "5040422134154", 10)
    client2 = Client(2, "nume", "6040422134154", 15)
    client_repo.store(client1)
    client_repo.store(client2)
    test_console = Console(book_controller, client_controller, rental_controller)
    report_list = test_console.most_active_clients_ui()

    assert report_list == [[15, client2], [10, client1]]


def test_least_rented_books():
    """
    functie de test pentru functia least_rented_books_report()
    """

    book_repo = BookInMemoryRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repo, book_validator)
    client_repo = ClientInMemoryRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repo, client_validator)
    rental_repo = RentalInMemoryRepository()
    rental_controller = RentalController(rental_repo)
    book1 = Book(1, "tit", "tit", "tit", "rented", 10)
    book2 = Book(2, "lop", "lop", "lop", "rented", 5)
    book_repo.store(book1)
    book_repo.store(book2)
    test_console = Console(book_controller, client_controller, rental_controller)
    report_list = test_console.least_rented_books_sorted()

    assert report_list == [[5, book2], [10, book1]]


def test_clients_and_books_sorted_by_name():
    """
    functie de test pentru functia clients_and_books_sorted_by_name_report()
    """

    book_repo = BookInMemoryRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repo, book_validator)
    client_repo = ClientInMemoryRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repo, client_validator)
    rental_repo = RentalInMemoryRepository()
    rental_controller = RentalController(rental_repo)
    book1 = Book(1, "tit", "tit", "tit", "available", 10)
    book2 = Book(2, "lop", "lop", "lop", "available", 5)
    book_repo.store(book1)
    book_repo.store(book2)
    client1 = Client(1, "nume1", "5040422134154", 0)
    client2 = Client(2, "nume2", "6040422134154", 0)
    client_repo.store(client1)
    client_repo.store(client2)
    rental1 = Rental(client1, book1)
    rental2 = Rental(client1, book2)
    rental_repo.store(rental1)
    rental_repo.store(rental2)
    test_console = Console(book_controller, client_controller, rental_controller)
    report_list = test_console.clients_and_books_sorted_by_name_report()

    assert report_list == [[2, client1], [0, client2]]


def test_clients_and_books_sorted_by_number():
    """
    functie de test pentru functia clients_and_books_sorted_by_number_of_books_report()
    """

    book_repo = BookInMemoryRepository()
    book_validator = BookValidator()
    book_controller = BookController(book_repo, book_validator)
    client_repo = ClientInMemoryRepository()
    client_validator = ClientValidator()
    client_controller = ClientController(client_repo, client_validator)
    rental_repo = RentalInMemoryRepository()
    rental_controller = RentalController(rental_repo)
    book1 = Book(1, "tit", "tit", "tit", "available", 10)
    book2 = Book(2, "lop", "lop", "lop", "available", 5)
    book_repo.store(book1)
    book_repo.store(book2)
    client1 = Client(1, "nume2", "5040422134154", 0)
    client2 = Client(2, "nume1", "6040422134154", 0)
    client_repo.store(client1)
    client_repo.store(client2)
    rental1 = Rental(client1, book1)
    rental2 = Rental(client1, book2)
    rental_repo.store(rental1)
    rental_repo.store(rental2)
    test_console = Console(book_controller, client_controller, rental_controller)
    report_list = test_console.clients_and_books_sorted_by_number_of_books_report()

    assert report_list == [[2, client1], [0, client2]]


def run_console_tests():
    test_most_rented_books()
    test_most_active_clients()
    test_least_rented_books()
    test_clients_and_books_sorted_by_name()
    test_clients_and_books_sorted_by_number()
