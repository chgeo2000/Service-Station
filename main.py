from Domain.CarValidator import CarValidator
from Domain.CardClientValidator import CardClientValidator
from Domain.TransactionValidator import TransactionValidator
from Repository.FileRepository import FileRepository
from Service.CarService import CarService
from Service.CardClientService import CardClientService
from Service.TransactionService import TransactionService
from Service.ExcelExportService import ExcelExportService
from Service.UndoService import UndoService
from UserInterface.Console import Console
from Tests.RunAll import run_all


def main():
    car_repository = FileRepository('cars.txt')
    card_client_repository = FileRepository('card_client.txt')
    transaction_repository = FileRepository('transactions.txt')

    car_validator = CarValidator()
    card_client_validator = CardClientValidator()
    transaction_validator = TransactionValidator()

    undo_redo_service = UndoService()
    car_service = CarService(car_repository, car_validator, transaction_repository, undo_redo_service)
    card_client_service = CardClientService(card_client_repository, card_client_validator, transaction_repository,
                                            undo_redo_service)
    transaction_service = TransactionService(transaction_repository, transaction_validator,
                                             car_repository, card_client_repository,
                                             undo_redo_service)
    excel_export_service = ExcelExportService(car_repository)

    user_interface = Console(car_service, card_client_service, transaction_service, excel_export_service,
                             undo_redo_service)
    user_interface.runMenu()


run_all()
main()




