from Domain.CarValidator import CarValidator
from Domain.CardClientValidator import CardClientValidator
from Domain.TransactionValidator import TransactionValidator
from Repository.FileRepository import FileRepository
from Service.CarService import CarService
from Service.CardClientService import CardClientService
from Service.TransactionService import TransactionService
from Service.UndoService import UndoService
from Tests.Utils import clear_file


def testGetTransactionsInInterval():
    clear_file("cars_test.txt")
    clear_file("cardclients_test.txt")
    clear_file("transactions_test.txt")

    cardclients_repository = FileRepository("cardclients_test.txt")
    transactions_repository = FileRepository("transactions_test.txt")
    cars_repository = FileRepository("cars_test.txt")

    transaction_validator = TransactionValidator()
    cardclient_validator = CardClientValidator()
    car_validator = CarValidator()

    undo_service = UndoService()

    cardclient_service = CardClientService(cardclients_repository, cardclient_validator, transactions_repository,
                                           undo_service)
    transaction_service = TransactionService(transactions_repository, transaction_validator, cars_repository,
                                             cardclients_repository, undo_service)
    cars_service = CarService(cars_repository, car_validator, transactions_repository, undo_service)

    cars_service.create("1", "bmw", 2008, 200000, "no")
    cars_service.create("2", "toyota", 2003, 300000, "no")
    cars_service.create("3", "ford", 2005, 380000, "no")

    cardclient_service.create("1", "Chira", "George", 50011137777, "13.11.2000", "13.11.2014")
    cardclient_service.create("2", "Chira", "Cosmin", 50011137778, "13.11.2000", "13.11.2014")
    cardclient_service.create("3", "Chira", "Alin", 50011137779, "13.11.2000", "13.11.2014")

    transaction_service.create("1", "1", "1", 200, 190, "2000.11.13", "15:20:30")
    transaction_service.create("2", "2", "1", 200, 175, "2000.11.13", "15:20:36")
    transaction_service.create("3", "3", "3", 200, 300, "2000.11.13", "15:20:42")

    assert transaction_service.getTransactionsInInterval(390, 600) == ["1", "3"]
