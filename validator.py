class BookValidator:
    def __init__(self):
        pass

    def validate_book(self, book):
        """
        validator pentru carti
        :param book: cartea de validat
        :raises ValueError: daca cartea nu este valida
        """

        errors = []

        if len(book.get_title()) < 2:
            errors.append("Titlul nu poate fi mai scurt de doua caractere!")

        if len(book.get_description()) < 2:
            errors.append("Descrierea nu poate fi mai scurta de doua caractere!")

        if len(book.get_author()) < 2:
            errors.append("Numele autorului nu poate fi mai scurt de doua caractere!")

        if book.get_is_rented() not in ['rented', 'available']:
            errors.append("Statusul cartii este incorect!")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)


class ClientValidator:
    def __init__(self):
        pass

    def validate_client(self, client):
        """
        validator pentru clienti
        :param client: clientul de validat
        :raises ValueError: daca clientul nu este valid
        """

        errors = []

        if len(client.get_name()) < 2:
            errors.append("Numele clientului nu poate fi mai scurt de 2 caractere!")

        if len(client.get_cnp()) != 13:
            errors.append("CNP-ul clientului trebuie sa aiba 13 caractere!")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
