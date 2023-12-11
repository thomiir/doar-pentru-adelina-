from service.book_service import BookController
from service.client_service import ClientController
from service.rentals_service import RentalController


class Console:
    def __init__(self, book_controller: BookController, client_controller: ClientController, rental_controller: RentalController):
        """
        initializeaza consola
        :param book_controller: controller-ul de carti
        :param client_controller: controller-ul de clienti
        :param rental_controller: controller-ul de inchirieri
        """

        self.__book_service = book_controller
        self.__client_service = client_controller
        self.__rentals_service = rental_controller

    def __print_main_menu(self):
        """
        printeaza meniul principal
        """

        print("Alegeti o optiune din meniul principal:")
        print("1. Meniul pentru carti.")
        print("2. Meniul pentru clienti.")
        print("3. Meniul pentru inchirieri")
        print("4. Meniul pentru rapoarte.")
        print("5. Genereaza X carti aleatorii.")
        print("6. Genereaza X clienti aleatorii.")
        print("7. Iesire.")

    def print_book_menu(self):
        """
        printeaza meniul pentru carti
        """
        
        print("Alegeti o optiune din meniul pentru carti:")
        print("1. Afiseaza lista curenta de carti.")
        print("2. Adauga o carte noua.")
        print("3. Modifica atributele unei carti existente.")
        print("4. Sterge o carte.")
        print("5. Cauta o carte dupa id.")
        print("6. Cauta o carte dupa titlu.")
        print("7. Iesire.")

    def print_client_menu(self):
        """
        printeaza meniul pentru clienti
        """

        print("Alegeti o optiune din meniul pentru clienti:")
        print("1. Afiseaza lista curenta de clienti.")
        print("2. Adauga un client nou.")
        print("3. Modifica atributele unui client existent.")
        print("4. Sterge un client.")
        print("5. Cauta un client dupa id.")
        print("6. Cauta un client dupa nume.")
        print("7. Iesire.")

    def print_rental_menu(self):
        """
        printeaza meniul pentru inchirieri
        """

        print("Alegeti o optiune din meniul pentru inchirieri:")
        print("1. Inchiriaza o carte.")
        print("2. Returneaza o carte.")
        print("3. Iesire")

    def print_report_menu(self):
        """
        printeaza meniul pentru rapoarte
        """

        print("Alegeti o optiune din meniul pentru rapoarte:")
        print("1. Genereaza raportul cu cele mai inchiriate carti.")
        print("2. Genereaza raportul cu cartile inchiriate de fiecare client, ordonat dupa numele clientilor.")
        print("3. Genereaza raportul cu cartile inchiriate de fiecare client, ordonat dupa numarul de carti inchiriate.")
        print("4. Genereaza raportul cu primii 20% dintre cei mai activi clienti.")
        print("5. Genereaza raportul cu ultimele 10% cele mai inchiriate carti")
        print("6. Iesire.")

    def print_book_list(self, book_list):
        """
        printeaza o lista de carti (in format string)
        :param book_list: lista de carti
        """

        for book in book_list:
            print(str(book))

    def print_client_list(self, client_list):
        """
        printeaza o lista de clienti (in format string)
        :param client_list: lista de clienti
        """

        for client in client_list:
            print(str(client))

    def delete_book_by_id_ui(self):
        """
        sterge o carte dupa id
        :raises ValueError: daca id-ul nu este valid
        """

        try:
            id = int(input("Introduceti id-ul cartii pe care doriti sa o stergeti: "))
            deleted_book = self.__book_service.delete_book(id)
            print("Cartea", str(deleted_book), "a fost stearsa cu succes!")

        except ValueError as ve:
            print(ve)

    def delete_client_by_id_ui(self):
        """
        sterge un client dupa id
        :raises ValueError: daca id-ul nu este valid
        """

        try:
            id = int(input("Introduceti id-ul clientului pe care doriti sa il stergeti: "))
            deleted_client = self.__client_service.delete_client(id)
            print("Clientul", str(deleted_client), "a fost sters cu succes!")

        except ValueError as ve:
            print(ve)

    def add_book_ui(self):
        """
        adauga o carte
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti id-ul cartii: ")
        title = input("Introduceti titlul cartii: ")
        description = input("Introduceti descrierea cartii: ")
        author = input("Introduceti autorul cartii: ")

        try:
            id = int(id)
            self.__book_service.add_book(id, title, description, author, "available", 0)
            print("Cartea a fost adaugata cu succes!")

        except ValueError as ve:
            print(ve)

    def add_client_ui(self):
        """
        adauga un client
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti id-ul clientului: ")
        name = input("Introduceti numele clientului: ")
        cnp = input("Introduceti CNP-ul clientului: ")

        try:
            id = int(id)
            self.__client_service.add_client(id, name, cnp, 0)
            print("Clientul a fost adaugat cu succes!")

        except ValueError as ve:
            print(ve)

    def update_book_ui(self):
        """
        modifica o carte
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti ID-ul cartii pe care doriti sa o modificati: ")
        title = input("Introduceti noul titlu al cartii: ")
        description = input("Introduceti noua descriere a cartii: ")
        author = input("Introduceti noul autor al cartii: ")
        is_rented = input("Introduceti noul status al cartii: ")
        no_rentals = input("Introduceti de cate ori a fost inchiriata cartea: ")
        try:
            id = int(id)
            self.__book_service.update_book(id, title, description, author, is_rented, no_rentals)
            print("Cartea a fost modificata cu succes!")

        except ValueError as ve:
            print(ve)

    def update_client_ui(self):
        """
        modifica un client
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti ID-ul clientului pe care doriti sa il modificati: ")
        name = input("Introduceti noul nume al clientului: ")
        cnp = input("Introduceti noul CNP al clientului: ")
        no_rentals = input("Introduceti numarul de inchirieri ale clientului de-a lungul timpului: ")
        try:
            id = int(id)
            self.__client_service.update_client(id, name, cnp)

        except ValueError as ve:
            print(ve)

    def search_book_by_id_ui(self):
        """
        cauta o carte dupa id
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti ID-ul cartii pe care doriti sa o cautati: ")

        try:
            id = int(id)
            filtered_books = self.__book_service.filter_by_id(id)
            if len(filtered_books) > 0:
                print("Cartea care are ID-ul dat este:")
                self.print_book_list(filtered_books)
            else:
                print("Nu exista carti cu ID-ul dat!")

        except ValueError:
            print("ID invalid!")

    def search_client_by_id_ui(self):
        """
        cauta un client dupa id
        :raises ValueError: daca id-ul nu este valid
        """

        id = input("Introduceti ID-ul clientului pe care doriti sa il cautati: ")

        try:
            id = int(id)
            filtered_clients = self.__client_service.filter_by_id(id)
            if len(filtered_clients) > 0:
                print("Clientul care are ID-ul dat este:")
                self.print_client_list(filtered_clients)
            else:
                print("Nu exista clienti cu ID-ul dat!")

        except ValueError:
            print("ID invalid!")

    def search_book_by_title_ui(self):
        """
        cauta o carte dupa titlu
        :raises ValueError: daca titlul nu este valid
        """

        title = input("Introduceti titlul cartii pe care doriti sa o cautati: ")
        filtered_books = self.__book_service.filter_by_title(title)

        try:
            if len(title) < 2:
                raise ValueError

            if len(filtered_books) > 0:
                print("Cartile cu titlul dat sunt: ")
                self.print_book_list(filtered_books)
            else:
                print("Nu exista carti cu titlul dat!")

        except ValueError:
            print("Titlul nu poate fi mai scurt de 2 caractere!")

    def search_client_by_name_ui(self):
        """
        cauta un client dupa nume
        :raises ValueError: daca numele nu este valid
        """

        name = input("Introduceti numele clientului pe care doriti sa il cautati: ")
        filtered_clients = self.__client_service.filter_by_name(name)

        try:
            if len(name) < 2:
                raise ValueError

            if len(filtered_clients) > 0:
                print("Clientii cu numele dat sunt: ")
                self.print_client_list(filtered_clients)
            else:
                print("Nu exista clienti cu numele dat!")

        except ValueError:
            print("Numele nu poate fi mai scurt de 2 caractere!")

    def rent_a_book_ui(self):
        """
        inchiriaza o carte
        :raises ValueError: daca unul dintre id-uri nu este valid
        :raises IndexError: daca statusul cartii este "rented" (deja este inchiriata)
        """

        client_id = input("Introduceti ID-ul clientului care inchiriaza cartea: ")
        book_id = input("Introduceti ID-ul cartii de inchiriat: ")

        try:
            client_id = int(client_id)
            book_id = int(book_id)
            client = self.__client_service.find_client_by_id(client_id)
            book = self.__book_service.find_book_by_id(book_id)
            if client is None or book is None:
                raise ValueError
            if book.get_is_rented() == "rented":
                raise IndexError
            self.__rentals_service.add_rental(client, book)
            self.__book_service.update_book(book.get_id(), book.get_title(), book.get_description(), book.get_author(), "rented", book.get_no_rentals() + 1)
            self.__client_service.update_client(client.get_id(), client.get_name(), client.get_cnp(), client.get_no_rentals() + 1)

        except ValueError:
            print("ID invalid!")

        except IndexError:
            print("Cartea a fost deja inchiriata!")

    def return_a_book_ui(self):
        """
        returneaza o carte
        :raises ValueError: daca unul dintre id-uri nu este valid
        """

        client_id = input("Introduceti ID-ul clientului care inchiriase cartea: ")
        book_id = input("Introduceti ID-ul cartii de inchiriat: ")

        try:
            client_id = int(client_id)
            book_id = int(book_id)
            client = self.__client_service.find_client_by_id(client_id)
            book = self.__book_service.find_book_by_id(book_id)
            if client is None or book is None:
                raise ValueError
            self.__rentals_service.delete_rental(client, book)
            self.__book_service.update_book(book.get_id(), book.get_title(), book.get_description(), book.get_author(), "available", book.get_no_rentals())

        except ValueError:
            print("ID invalid!")

    def most_rented_books_report_ui(self):
        """
        creeaza raportul cu cele mai inchiriate carti
        :return: raportul cu cele mai inchiriate carti
        """

        report_list = []
        for book in self.__book_service.get_all_books():
            number = book.get_no_rentals()
            report_list.append([number, book])
        report_list = self.__client_service.sort_by_number_of_books(report_list)
        return report_list

    def most_active_clients_ui(self):
        """
        creeaza raportul cu primii 20% dintre cei mai activi clienti
        :return: raportul cu primii 20% dintre cei mai activi clienti
        """

        report_list = []
        for client in self.__client_service.get_all_clients():
            number = client.get_no_rentals()
            report_list.append([number, client])
        report_list = self.__client_service.sort_by_number_of_books(report_list)
        return report_list

    def clients_and_books_sorted_by_name_report(self):
        """
        creeaza raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa nume
        :return: raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa nume
        """
        
        report_list = []
        for client in self.__client_service.get_all_clients():
            number = self.__rentals_service.find_number_of_books_by_client(client.get_id())
            report_list.append([number, client])
        report_list = self.__client_service.sort_by_name(report_list)
        return report_list

    def clients_and_books_sorted_by_number_of_books_report(self):
        """
        creeaza raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa numarul de carti
        :return: raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa numarul de carti
        """

        report_list = []
        for client in self.__client_service.get_all_clients():
            number = self.__rentals_service.find_number_of_books_by_client(client.get_id())
            report_list.append([number, client])
        report_list = self.__client_service.sort_by_number_of_books(report_list)
        return report_list

    def least_rented_books_sorted(self):
        """
        creeaza raportul cu cele mai putin inchiriate carti, ordonat descrescator dupa numarul de inchirieri
        :return: raportul cu cele mai putin inchiriate carti, ordonat descrescator dupa numarul de inchirieri
        """

        report_list = []
        for book in self.__book_service.get_all_books():
            number = book.get_no_rentals()
            report_list.append([number, book])
        report_list = self.__book_service.sort_by_number_of_books(report_list)
        return report_list

    def print_report_list_sorted_by_number(self, report_list):
        """
        printeaza raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa numarul de carti
        :param report_list: raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa numarul de carti
        """

        print("Raportul care contine lista de clienti, precum si numarul de carti inchiriate pe care le au acestia, ordonata dupa numarul de carti este:")
        for i in range(0,len(report_list)):
            if report_list[i][0] != 0:
                print(report_list[i][1].get_name(), report_list[i][0])

    def print_report_list_sorted_by_name(self, report_list):
        """
        printeaza raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa nume
        :param report_list: raportul cu clientii si numarul de carti inchiriate de acestia, ordonat dupa nume
        """

        print("Raportul care contine lista de clienti, precum si numarul de carti inchiriate pe care le au acestia, ordonata dupa numele clientilor este:")
        for i in range(0, len(report_list)):
            if report_list[i][0] != 0:
                print(report_list[i][1].get_name(), report_list[i][0])

    def print_most_rented_books(self, report_list):
        """
        printeaza raportul cu cele mai inchiriate carti
        :param report_list: raportul cu cele mai inchiriate carti
        """

        print("Raportul care contine cele mai inchiriate carti este: ")
        print(report_list[0][1].get_title(), report_list[0][0])
        i = 1
        while report_list[i][0] == report_list[0][0]:
            print(report_list[i][1].get_title(), report_list[i][0])
            i = i + 1

    def print_most_active_clients(self, report_list):
        """
        printeaza raportul cu primii 20% dintre cei mai activi clienti
        :param report_list: raportul cu primii 20% dintre cei mai activi clienti
        """

        print("Raportul care contine primii 20% cei mai activi clienti este: ")
        length = int(1/5 * len(report_list))
        i = 0
        while length >  0 and i < len(report_list):
            j = i
            if (report_list[i][0] != 0):
                print(report_list[i][1].get_name(), report_list[i][0])
            while report_list[j][0] == report_list[j + 1][0]:
                if (report_list[j + 1][0]):
                    print(report_list[j + 1][1].get_name(), report_list[j + 1][0])
                j = j + 1
            i = j + 1
            length = length - 1

    def print_least_rented_books(self, report_list):
        """
        printeaza raportul cu ultimele 10% dintre cele mai inchiriate carti
        :param report_list:  raportul cu ultimele 10% dintre cele mai inchiriate carti
        """

        print("Raportul care contine ultimele 10% dintre cele mai inchiriate carti este: ")
        length = int(1 / 10 * len(report_list))
        i = len(report_list) - 1
        list = []
        while length > 0 and i >= 0:
            j = i
            list.append([report_list[i][1].get_title(), report_list[i][1].get_author(), report_list[i][0]])
            while report_list[j][0] == report_list[j - 1][0]:
                list.append([report_list[j - 1][1].get_title(), report_list[j - 1][1].get_author(), report_list[j - 1][0]])
                j = j - 1
            i = j - 1
            length = length - 1

        i = len(list) - 1
        while i >= 0:
            print (list[i])
            i =  i - 1

    def generate_random_books_ui(self):
        """
        generarea aleatoare a entitatilor de tip Book
        :raises: ValueError daca numarul este invalid
        """

        self.__book_service.delete_all_books()

        number = input("Introduceti numarul de carti de generat: ")
        try:
            number = int(number)
            if number < 1:
                raise ValueError
            self.__book_service.generate_random_books(number)

        except ValueError:
            print("Numar invalid!")

    def generate_random_clients_ui(self):
        """
        generarea aleatoare a entitatilor de tip Client
        :raises: ValueError daca numarul este invalid
        """
        self.__client_service.delete_all_clients()

        number = input("Introduceti numarul de clienti de generat: ")
        try:
            number = int(number)
            if number < 1:
                raise ValueError
            self.__client_service.generate_random_clients(number)

        except ValueError:
            print("Numar invalid!")

    def run(self):
        """
        functia principala a consolei
        """
        
        while True:
            self.__print_main_menu()
            option = input()
            if option == "1":
                while True:
                    self.print_book_menu()
                    sub_option = input()
                    if sub_option == "1":
                        print("Lista curenta de carti este:")
                        self.print_book_list(self.__book_service.get_all_books())
                    elif sub_option == "2":
                        self.add_book_ui()
                    elif sub_option == "3":
                        self.update_book_ui()
                    elif sub_option == "4":
                        self.delete_book_by_id_ui()
                    elif sub_option == "5":
                        self.search_book_by_id_ui()
                    elif sub_option == "6":
                        self.search_book_by_title_ui()
                    else:
                        break

            elif option == "2":
                while True:
                    self.print_client_menu()
                    sub_option = input()
                    if sub_option == "1":
                        print("Lista curenta de clienti este:")
                        self.print_client_list(self.__client_service.get_all_clients())
                    elif sub_option == "2":
                        self.add_client_ui()
                    elif sub_option == "3":
                        self.update_client_ui()
                    elif sub_option == "4":
                        self.delete_client_by_id_ui()
                    elif sub_option == "5":
                        self.search_client_by_id_ui()
                    elif sub_option == "6":
                        self.search_client_by_name_ui()
                    else:
                        break
            elif option == "3":
                while True:
                    self.print_rental_menu()
                    sub_option = input()
                    if sub_option == "1":
                        self.rent_a_book_ui()
                    elif sub_option == "2":
                        self.return_a_book_ui()
                    else:
                        break

            elif option == "4":
                while True:
                    self.print_report_menu()
                    sub_option = input()
                    if sub_option == "1":
                        self.print_most_rented_books(self.most_rented_books_report_ui())
                    elif sub_option == "2":
                        self.print_report_list_sorted_by_name(self.clients_and_books_sorted_by_name_report())
                    elif sub_option == "3":
                        self.print_report_list_sorted_by_number(self.clients_and_books_sorted_by_number_of_books_report())
                    elif sub_option == "4":
                        self.print_most_active_clients(self.most_active_clients_ui())
                    elif sub_option == "5":
                        self.print_least_rented_books(self.least_rented_books_sorted())
                    else:
                        break

            elif option == "5":
                self.generate_random_books_ui()

            elif option == "6":
                self.generate_random_clients_ui()

            elif option == "7":
                break

            else:
                print("Optiune invalida!")
