from Domain.CarValidator import CarValidator
from Domain.CardClientValidator import CardClientValidator
from Domain.TransactionValidator import TransactionValidator
from Service.CarService import CarService
from Service.CardClientService import CardClientService
from Service.TransactionService import TransactionService
from Tests.Utils import *
from Repository.FileRepository import *
from Service.UndoService import UndoService


def testMergeSort():
    """
    Tests merge sort method.
    Merge sort is used to sort a list with tuples as elements in descending order by the second element of the tuple.
    """
    clear_file("cars_test.txt")
    clear_file("transactions_test.txt")

    cars_repository = FileRepository("cars_test.txt")
    transactions_repository = FileRepository("transactions_test.txt")

    car_validator = CarValidator()

    undo_service = UndoService()

    cars_service = CarService(cars_repository, car_validator, transactions_repository, undo_service)

    test_array = [("ford", 2), ("bmw", 3), ("toyota", 1)]
    assert cars_service.merge_sort(test_array, lambda tuple: tuple[1]) == [("bmw", 3), ("ford", 2), ("toyota", 1)]


def testDOByWorkmanship():
    """
    Tests "DOByWorkmanship" method
    :return:
    """

    clear_file("cars_test.txt")
    clear_file("transactions_test.txt")
    clear_file("cardclients_test.txt")

    cars_repository = FileRepository("cars_test.txt")
    transactions_repository = FileRepository("transactions_test.txt")
    cardclients_repository = FileRepository("cardclients_test.txt")

    car_validator = CarValidator()
    transaction_validator = TransactionValidator()
    cardclient_validator = CardClientValidator()

    undo_service = UndoService()

    cars_service = CarService(cars_repository, car_validator, transactions_repository, undo_service)
    cardclient_service = CardClientService(cardclients_repository, cardclient_validator, transactions_repository,
                                           undo_service)
    transaction_service = TransactionService(transactions_repository, transaction_validator, cars_repository,
                                             cardclients_repository, undo_service)

    cars_service.create("1", "bmw", 2008, 200000, "no")
    cars_service.create("2", "toyota", 2003, 300000, "no")
    cars_service.create("3", "ford", 2005, 380000, "no")

    cardclient_service.create("1", "Chira", "George", 50011137777, "13.11.2000", "13.11.2014")
    cardclient_service.create("2", "Chira", "Cosmin", 50011137778, "13.11.2000", "13.11.2014")
    cardclient_service.create("3", "Chira", "Alin", 50011137779, "13.11.2000", "13.11.2014")

    transaction_service.create("1", "1", "1", 200, 300, "2000.11.13", "15:20:30")
    transaction_service.create("2", "2", "2", 200, 175, "2000.11.13", "15:20:36")
    transaction_service.create("3", "3", "3", 200, 190, "2000.11.13", "15:20:42")

    assert cars_service.DObyWorkmanship() == [("bmw", 300), ("ford", 190), ("toyota", 175)]


def testPopulateCars():
    clear_file("cars_test.txt")
    clear_file("transactions_test.txt")

    cars_repository = FileRepository("cars_test.txt")
    transactions_repository = FileRepository("transactions_test.txt")

    car_validator = CarValidator()

    undo_service = UndoService()

    cars_service = CarService(cars_repository, car_validator, transactions_repository, undo_service)

    cars_service.populate_cars(15)

    assert len(cars_service.get_all()) == 15
