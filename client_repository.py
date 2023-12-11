from domain.client import Client


class ClientInMemoryRepository:
    def __init__(self):
        """
        initializeaza lista de clienti
        """

        self.__client_list = []

    def store(self, client: Client):
        """
        adauga un client in lista de clienti
        :param client: clientul de adaugat
        :raises ValueError: daca exista deja un client cu acelasi id sau cnp
        """

        if self.find_by_id(client.get_id()):
            raise ValueError("Exista deja un client cu acest id!")
        if self.find_by_cnp(client.get_cnp()):
            raise ValueError("Exista deja un client cu acest cnp!")
        self.__client_list.append(client)

    def find_by_id(self, id):
        """
        cauta un client dupa id
        :param id: id-ul clientului de cautat
        :return: clientul cu id-ul dat sau None daca nu exista
        """

        for client in self.__client_list:
            if client.get_id() == id:
                return client
        return None

    def find_by_cnp(self, cnp):
        """
        cauta un client dupa cnp
        :param cnp: cnp-ul clientului de cautat
        :return: clientul cu cnp-ul dat sau None daca nu exista
        """

        for client in self.__client_list:
            if client.get_cnp() == cnp:
                return client
        return None

    def update(self, id, new_client):
        """
        modifica un client
        :param id: id-ul clientului de modificat
        :param new_client: noul client
        :raises ValueError: daca nu exista un client cu id-ul dat
        """

        client_to_update = self.find_by_id(id)
        if client_to_update is None:
            raise ValueError("Nu exista un client cu acest id!")
        self.__client_list[self.__client_list.index(client_to_update)] = new_client

    def delete(self, id):
        """
        sterge un client
        :param id: id-ul clientului de sters
        :raises ValueError: daca nu exista un client cu id-ul dat
        :return: clientul sters (pentru afisare)
        """

        client_to_delete = self.find_by_id(id)
        if client_to_delete is None:
            raise ValueError("Nu exista un client cu acest id!")
        self.__client_list.remove(client_to_delete)
        return client_to_delete

    def get_current_list(self):
        """
        getter pentru lista de clienti
        :return: lista de clienti
        """

        return self.__client_list

    def size(self):
        """
        getter pentru lungimea listei de clienti
        :return: lungimea listei de clienti
        """
        
        return len(self.__client_list)

    def delete_all_clients(self):
        for i in range(0, len(self.get_current_list())):
            self.delete(i)