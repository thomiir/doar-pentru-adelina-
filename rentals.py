from domain.book import Book
from domain.client import Client


class Rental:
    def __init__(self, client: Client, book: Book):
        """
        Initializeaza un obiect de tip Rental cu valorile date
        *practic rental este legatura dintre clasele client si book
        :param client: clientul / tip Client
        :param book: cartea / Tip Book
        """
        self.__client = client
        self.__book = book

    def get_client(self):
        """
        getter pentru client
        :return: clientul
        """

        return self.__client

    def get_book(self):
        """
        getter pentru carte
        :return: cartea
        """
        
        return self.__book
