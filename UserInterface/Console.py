import datetime

from Service.CarService import CarService
from Service.CardClientService import CardClientService
from Service.TransactionService import TransactionService
from Service.ExcelExportService import ExcelExportService
from Service.UndoService import UndoService


class Console:
    def __init__(self, car_service: CarService,
                 card_client_service: CardClientService,
                 transaction_service: TransactionService,
                 excel_export_service: ExcelExportService,
                 undo_service: UndoService):
        self.__car_service = car_service
        self.__card_client_service = card_client_service
        self.__transaction_service = transaction_service
        self.__excel_export_service = excel_export_service
        self.__undo_service = undo_service

    def showMenu(self):
        print('1. CRUD Car')
        print('2. CRUD Card Client')
        print('3. CRUD Transaction')
        print('4. Search cars or cards')
        print('5. Populate cars')
        print('6. Show transactions with sum in interval')
        print('f. Show transactions with sum in interval using filter')
        print('7. Show cars ordered descending after sum workmanship')
        print('8. Show cards ordered descending after discount ')
        print('z. Show cards ordered descending after discount using zip')
        print('9. Delete all transactions in interval')
        print('10. Update warranties of old cars')
        print('11. Export cars to excel')
        print('x. Exit')

    def runMenu(self):

        while True:
            self.showMenu()
            option = input('Choose option: ')
            if option == '1':
                self.run_crud_cars()
            elif option == '2':
                self.run_crud_card_client()
            elif option == '3':
                self.run_crud_transaction()
            elif option == '4':
                self.search_cars_or_cards()
            elif option == '5':
                self.handle_populate_cars()
            elif option == '6':
                self.handle_show_transactions_in_interval()
            elif option == 'f':
                self.handle_show_transactions_in_interval_using_filter()
            elif option == '7':
                self.handle_show_cars_in_descending_order()
            elif option == '8':
                self.handle_show_cards_in_descending_order()
            elif option == 'z':
                self.handle_show_cards_in_descending_order_using_zip()
            elif option == '9':
                self.handle_delete_transactions_in_interval()
            elif option == '10':
                self.handle_update_warranties()
            elif option == '11':
                self.export_cars_to_excel()
            elif option == 'x':
                break
            else:
                print('Incorrect option. Try again: ')

    def run_crud_cars(self):
        while True:
            print('1. Create car.')
            print('2. Delete car.')
            print('3. Update car.')
            print('4. Show all cars.')
            print('u. Undo')
            print('b. Back')
            option = input('Choose option: ')
            if option == '1':
                self.handle_create_car()
            elif option == '2':
                self.handle_delete_car()
            elif option == '3':
                self.handle_update_car()
            elif option == '4':
                self.handle_show_all_cars()
            elif option == 'u':
                self.__undo_service.do_undo()
            elif option == 'b':
                break
            else:
                print('Incorrect option. Try again: ')

    def handle_create_car(self):
        try:
            id_car = input('Id: ')
            model = input('Model: ')
            purchase_year = int(input('Purchase_year: '))
            km_travelled = int(input('Km_travelled: '))
            in_warranty = input('In_warranty (yes / no): ')

            self.__car_service.create(id_car, model, purchase_year, km_travelled, in_warranty)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_delete_car(self):
        try:
            id_car = input('Id of the car you want to delete: ')
            self.__car_service.delete(id_car)

        except KeyError as ke:
            print(ke)

    def handle_update_car(self):
        try:
            id_car = input('Id: ')
            model = input('Model: (empty if you dont want to change it)')
            purchase_year = int(input('Purchase_year: (empty if you dont want to change it)'))
            km_travelled = int(input('Km_travelled: (empty if you dont want to change it) '))
            in_warranty = input('In_warranty (yes / no): (empty if you dont want to change it)')

            self.__car_service.update(id_car, model, purchase_year, km_travelled, in_warranty)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_cars(self):
        for car in self.__car_service.get_all():
            print(car)

    def run_crud_card_client(self):
        while True:
            print('1. Create card client.')
            print('2. Delete card client.')
            print('3. Update card client.')
            print('4. Show all cards.')
            print('u. Undo')
            print('b. Back')
            option = input('Choose option: ')
            if option == '1':
                self.handle_create_card_client()
            elif option == '2':
                self.handle_delete_card_client()
            elif option == '3':
                self.handle_update_card_client()
            elif option == '4':
                self.handle_show_all_cards()
            elif option == 'u':
                self.__undo_service.do_undo()
            elif option == 'b':
                break
            else:
                print('Incorrect option. Try again: ')

    def handle_create_card_client(self):
        try:
            id_card = input('Id: ')
            surname = input('Surname:  ')
            firstname = input('First name: ')
            cnp = int(input('Cnp: '))
            birthdate = input('Birthdate: ')
            registration_date = input("Registration date: ")

            self.__card_client_service.create(id_card, surname, firstname, cnp, birthdate, registration_date)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_delete_card_client(self):
        try:
            id_card = input('Id of the card you want to delete: ')
            self.__card_client_service.delete(id_card)

        except KeyError as ke:
            print(ke)

    def handle_update_card_client(self):
        try:
            id_card = input('Id: (empty if you dont want to change it)')
            surname = input('Surname: (empty if you dont want to change it)')
            firstname = int(input('First name: (empty if you dont want to change it)'))
            cnp = int(input('Cnp: (empty if you dont want to change it)'))
            birthdate = input('Birthdate: (empty if you dont want to change it)')
            registration_date = input("Registration date: (empty if you dont want to change it)")

            self.__card_client_service.update(id_card, surname, firstname, cnp, birthdate, registration_date)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_cards(self):
        for card_client in self.__card_client_service.get_all():
            print(card_client)

    def run_crud_transaction(self):
        while True:
            print('1. Create transaction.')
            print('2. Delete transaction.')
            print('3. Update transaction.')
            print('4. Show all transactions.')
            print('u. Undo')
            print('b. Back')
            option = input('Choose option: ')
            if option == '1':
                self.handle_create_transaction()
            elif option == '2':
                self.handle_delete_transaction()
            elif option == '3':
                self.handle_update_transaction()
            elif option == '4':
                self.handle_show_all_transactions()
            elif option == 'u':
                self.__undo_service.do_undo()
            elif option == 'b':
                break
            else:
                print('Incorrect option. Try again: ')

    def handle_create_transaction(self):
        try:
            id_transaction = input("Id: ")
            id_car = input("Id car: ")
            id_card = input("Id card: ")
            sum_pieces = int(input("Sum pieces: "))
            sum_workmanship = int(input("Sum workmanship: "))
            date = input("Date (YYYY.MM.DD):  ")
            hour = input("Hour (HH:MM:SS): ")

            """
                        for car in self.__car_service.get_all():
                if id_car == car.id_entity and car.in_warranty is True:
                    sum_pieces = 0

            for card in self.__card_client_service.get_all():
                if id_card == card.id_entity:
                    sum_workmanship = sum_workmanship - sum_workmanship * (1/10)
            """

            self.__transaction_service.create(id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_delete_transaction(self):
        try:
            id_transaction = input('Id of the transaction you want to delete: ')
            self.__transaction_service.delete(id_transaction)

        except KeyError as ke:
            print(ke)

    def handle_update_transaction(self):
        
        try:
            id_transaction = input('Id: (empty if you dont want to change it)')
            id_car = input('Id car: (empty if you dont want to change it)')
            id_card = input('Id card: (empty if you dont want to change it)')
            sum_pieces = int(input('Sum pieces: (empty if you dont want to change it)'))
            sum_workmanship = int(input('Birthdate: (empty if you dont want to change it)'))
            date = input("Date: (empty if you dont want to change it)")
            hour = input("Hour: (empty if you dont want to change it)")
    
            self.__transaction_service.update(id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_transactions(self):
        for transaction in self.__transaction_service.get_all():
            print(transaction)

    def handle_populate_cars(self):

        number_of_cars = int(input("How many cars do you want to add? "))

        self.__car_service.populate_cars(number_of_cars)

    def handle_show_cars_in_descending_order(self):

        for elem in self.__car_service.DObyWorkmanship():
            print(f"Sum workmanship of the car:{elem[0]} is: {elem[1]} RON")

    def search_cars_or_cards(self):
        while True:
            print('1. Search car.')
            print('2. Search card client.')
            print('b. Back.')

            option = input('Choose option: ')
            if option == '1':
                self.handle_search_car()
            elif option == '2':
                self.handle_search_card_client()
            elif option == 'b':
                break
            else:
                print('Incorrect option. Try again: ')

    def handle_search_car(self):
        model = input("Give the model of the car you are looking for: ")

        list_of_cars = []

        for car in self.__car_service.get_all():
            if car.model == model:
                list_of_cars.append(car)

        for elem in list_of_cars:
            print(elem.__str__())

        if len(list_of_cars) > 1:
            purchase_year = int(input("Give the purchase year of the car you are looking for: "))
            new_list_of_cars = []

            for elem in list_of_cars:
                if elem.purchase_year == purchase_year:
                    new_list_of_cars.append(elem)

            for elem in new_list_of_cars:
                print(elem.__str__())
        else:
            print(f'That s the only {model} we have.')

        if len(list_of_cars) > 1 and len(new_list_of_cars) > 1:
            km_travelled = int(input("Give the km travelled of the car you are looking for: "))
            last_list_of_cars = []
            for elem in new_list_of_cars:
                if elem.km_travelled == km_travelled:
                    last_list_of_cars.append(elem)

            for elem in last_list_of_cars:
                print(elem.__str__())

    def handle_search_card_client(self):
        surname = input("Give the surname of the client you are looking for: ")

        list_of_clients = []

        for client in self.__card_client_service.get_all():
            if client.surname == surname:
                list_of_clients.append(client)

        for elem in list_of_clients:
            print(elem.__str__())

        if len(list_of_clients) > 1:
            firstname = input("Give the firstname of the client you are looking for: ")
            new_list_of_clients = []

            for elem in list_of_clients:
                if elem.firstname == firstname:
                    new_list_of_clients.append(elem)

            for elem in new_list_of_clients:
                print(elem.__str__())
        else:
            print(f'We have only one person with the surname: {surname}')

        if len(list_of_clients) > 1 and len(new_list_of_clients) > 1:
            cnp = int(input("Give the cnp of the client you are looking for: "))
            last_list_of_clients = []
            for elem in new_list_of_clients:
                if elem.cnp == cnp:
                    last_list_of_clients.append(elem)

            for elem in last_list_of_clients:
                print(elem.__str__())

    def handle_show_transactions_in_interval(self):
        start_interval = int(input("Give the inferior limit of the interval: "))
        end_interval = int(input("Give the superior limit of the interval: "))
        print("Transactions with the following id-s respect the condition imposed: ")
        for elem in self.__transaction_service.getTransactionsInInterval(start_interval, end_interval):
            print(elem)

    def handle_show_transactions_in_interval_using_filter(self):
        start_interval = int(input("Give the inferior limit of the interval: "))
        end_interval = int(input("Give the superior limit of the interval: "))
        for elem in self.__transaction_service.getTransactionsInIntervalUsingFilter(start_interval, end_interval):
            print(elem)

    def handle_show_cards_in_descending_order(self):
        for elem in self.__card_client_service.DObyDiscount():
            print(f"The card of:{elem[0]}, {elem[1]} offered a {elem[2]} RON discount. ")

    def handle_show_cards_in_descending_order_using_zip(self):
        for elem in self.__card_client_service.DObyDiscountUsingZip():
            print(f"The following card:{elem[0]} offered a {elem[1]} RON discount. ")

    def handle_delete_transactions_in_interval(self):

        start_interval = input("Start interval: ")
        end_interval = input("End interval: ")
        for transaction in self.__transaction_service.deleteTransactionsInInterval(start_interval, end_interval):
            self.__transaction_service.delete(transaction.id_entity)

    def handle_update_warranties(self):
        current_year = datetime.datetime.now().year
        model = ''
        purchase_year = ''
        km_travelled = ''
        in_warranty = 'no'

        for elem in self.__car_service.updateWarranty(current_year):
            self.__car_service.update(elem.id_entity, model, purchase_year, km_travelled, in_warranty)

    def export_cars_to_excel(self):
        self.__excel_export_service.export()
