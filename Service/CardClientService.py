from Domain.AddOperation import AddOperation
from Domain.CardClient import CardClient
from Domain.CardClientValidator import CardClientValidator
from Domain.DeleteOperation import DeleteOperation
from Repository.FileRepository import FileRepository
from Service.UndoService import UndoService


class CardClientService:
    def __init__(self, card_client_repository: FileRepository, card_client_validator: CardClientValidator,
                 transaction_repository: FileRepository,
                 undo_service: UndoService):
        self.__card_client_repository = card_client_repository
        self.__card_client_validator = card_client_validator
        self.__transaction_repository = transaction_repository
        self.__undo_service = undo_service

    def create(self, id_card, surname, firstname, cnp, birthdate, registration_date):
        """
        It adds a CardClient in the storage dict.
        :param id_card: int, id_card
        :param surname: string, surname
        :param firstname: int, firstname
        :param cnp: int, cnp
        :param birthdate: string, birthdate
        :param registration_date: string, registration_date
        """

        card_client = CardClient(id_card, surname, firstname, cnp, birthdate, registration_date)
        self.__card_client_validator.validate(card_client)

        cnp = card_client.cnp
        for a_card_client in self.__card_client_repository.get_all():
            if cnp == a_card_client.cnp:
                raise KeyError(f'The following CNP: {cnp} already exists.')

        self.__card_client_repository.create(card_client)
        self.__undo_service.add_to_undo(AddOperation(self.__card_client_repository, card_client))

    def delete(self, id_card):
        card_client = self.__card_client_repository.find_by_id(id_card)
        self.__card_client_repository.delete(id_card)
        self.__undo_service.add_to_undo(DeleteOperation(self.__card_client_repository, card_client))

    def update(self, id_card, surname, firstname, cnp, birthdate, registration_date):
        card_client = self.__card_client_repository.find_by_id(id_card)
        if card_client is None:
            raise KeyError(f"The card client with id: {id_card} doesn't exist.")

        if surname != '':
            card_client.surname = surname
        if firstname != '':
            card_client.firstname = firstname
        if cnp != '':
            card_client.cnp = cnp
        if birthdate != '':
            card_client.birthdate = birthdate
        if registration_date != '':
            card_client.registration_date = registration_date

        self.__card_client_validator.validate(card_client)

        for a_card_client in self.__card_client_repository.get_all():
            if cnp == a_card_client.cnp:
                raise KeyError(f'The following CNP: {cnp} already exists.')

        self.__card_client_repository.update(card_client)

    def get_all(self):
        return self.__card_client_repository.get_all()

    def DObyDiscount(self):
        result = []
        for card_client in self.__card_client_repository.get_all():
            discount = 0
            for transaction in self.__transaction_repository.get_all():
                if card_client.id_entity == transaction.id_card:
                    discount += transaction.sum_workmanship * (1/10)
            result.append((card_client.surname, card_client.firstname, discount))
        output = sorted(result, key=lambda tuple: tuple[2], reverse=True)
        return output

    def DObyDiscountUsingZip(self):
        list_of_discounts = []
        list_of_all_cards = []
        for card_client in self.__card_client_repository.get_all():
            discount = 0
            for transaction in self.__transaction_repository.get_all():
                if card_client.id_entity == transaction.id_card:
                    initial_sum_workmanship = (10*transaction.sum_workmanship)/9
                    discount += initial_sum_workmanship - transaction.sum_workmanship
                list_of_discounts.append(discount)

        for card in self.__card_client_repository.get_all():
            list_of_all_cards.append(card)

        mapped = list(zip(list_of_all_cards, list_of_discounts))
        output = sorted(mapped, key=lambda value: value[1], reverse=True)
        return output
