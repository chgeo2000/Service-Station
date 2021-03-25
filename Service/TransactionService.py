from Domain.AddOperation import AddOperation
from Domain.DeleteOperation import DeleteOperation
from Domain.Transaction import Transaction
from Domain.TransactionValidator import TransactionValidator
from Repository.FileRepository import FileRepository
from Service.UndoService import UndoService
from ViewModels.Transaction_ViewModel import TransactionViewModel


class TransactionService:
    def __init__(self,
                 transactions_repository: FileRepository,
                 transaction_validator: TransactionValidator,
                 cars_repository: FileRepository,
                 card_clients_repository: FileRepository,
                 undo_service: UndoService):
        self.__transactions_repository = transactions_repository
        self.__transaction_validator = transaction_validator
        self.__cars_repository = cars_repository
        self.__card_clients_repository = card_clients_repository
        self.__undo_service = undo_service

    def create(self, id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour):

        transaction = Transaction(id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour)

        if self.__cars_repository.find_by_id(id_car) is None:
            raise KeyError(f"It doesn't exist any car with this id: {id_car}")

        if self.__card_clients_repository.find_by_id(id_card) is None:
            raise KeyError(f"It doesn't exist any card with this id: {id_card}")

        self.__transaction_validator.validate(transaction)

        self.__transactions_repository.create(transaction)
        self.__undo_service.add_to_undo(AddOperation(self.__transactions_repository, transaction))

    def delete(self, id_transaction):
        transaction = self.__transactions_repository.find_by_id(id_transaction)
        self.__transactions_repository.delete(id_transaction)
        self.__undo_service.add_to_undo(DeleteOperation(self.__transactions_repository, transaction))

    def update(self, id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour):
        transaction = self.__transactions_repository.find_by_id(id_transaction)
        if transaction is None:
            raise KeyError(f"The transaction with id: {id_transaction} doesn't exist.")

        if id_car != '':
            if self.__cars_repository.find_by_id(id_car) is None:
                raise KeyError(f'We cannot update the transaction because a car with the id: {id_car} doesnt exist')
            transaction.id_car = id_car
        if id_card != '':
            if self.__card_clients_repository.find_by_id(id_card) is None:
                raise KeyError(f'We cannot update the transaction because a card with the id: {id_card} doesnt exist')
            transaction.id_card = id_card
        if sum_pieces != '':
            transaction.sum_pieces = sum_pieces
        if sum_workmanship != '':
            transaction.sum_workmanship = sum_workmanship
        if date != '':
            transaction.date = date
        if hour != '':
            transaction.hour = hour

        self.__transaction_validator.validate(transaction)

        self.__transactions_repository.update(transaction)

    def get_all(self):
        view_models = []
        for transaction in self.__transactions_repository.get_all():
            car = self.__cars_repository.find_by_id(transaction.id_car)
            card_client = self.__card_clients_repository.find_by_id(transaction.id_card)
            view_models.append(TransactionViewModel(transaction.id_entity, car, card_client, transaction.sum_pieces,
                                                    transaction.sum_workmanship, transaction.date, transaction.hour))

        return view_models

    def getTransactionsInInterval(self, start_interval, end_interval):
        output = []
        for transaction in self.__transactions_repository.get_all():
            sum = transaction.sum_pieces + transaction.sum_workmanship
            if start_interval <= sum <= end_interval:
                output.append(transaction.id_entity)
        return output

    def getTransactionsInIntervalUsingFilter(self, start_interval, end_interval):
        transactions = self.__transactions_repository.get_all()
        output = list(filter(lambda a_transaction: start_interval <= a_transaction.sum_pieces + a_transaction.sum_workmanship <= end_interval, transactions))
        return output

    def deleteTransactionsInInterval(self, start_interval, end_interval):
        output = []
        day_start, month_start, year_start = start_interval.split('.')
        day_end, month_end, year_end = end_interval.split(".")

        for transaction in self.__transactions_repository.get_all():
            date = transaction.date
            day, month, year = date.split('.')

            if (
                    (int(year_start) <= int(year) < int(year_end))
                    or ((int(year_start) <= int(year) <= int(year_end)) and (
                    int(month_start) <= int(month) < int(month_end)))
                    or ((int(year_start) <= int(year) <= int(year_end)) and (
                    int(month_start) <= int(month) <= int(month_end)) and (int(day_start) <= int(day) < int(day_end)))

            ):
                output.append(transaction)

        return output
