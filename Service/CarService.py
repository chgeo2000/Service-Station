from Domain.AddOperation import AddOperation
import random
from Domain.DeleteOperation import DeleteOperation
from Domain.Car import Car
from Domain.CarValidator import CarValidator
from Repository.FileRepository import FileRepository
from Service.UndoService import UndoService


class CarService:
    def __init__(self, cars_repository: FileRepository, car_validator: CarValidator,
                 transaction_repository: FileRepository,
                 undo_service: UndoService):
        self.__cars_repository = cars_repository
        self.__car_validator = car_validator
        self.__transaction_repository = transaction_repository
        self.__undo_service = undo_service

    def create(self, id_car, model, purchase_year, km_travelled, in_warranty):
        """
        It adds a car in the storage dict.
        :param id_car: int, an_id
        :param model: string, a model
        :param purchase_year: int, the purchase_year
        :param km_travelled: int, km_travelled
        :param in_warranty: boolean, in_warranty
        """

        car = Car(id_car, model, purchase_year, km_travelled, in_warranty)
        self.__car_validator.validate(car)

        if in_warranty == 'yes':
            car.in_warranty = True
        else:
            car.in_warranty = False

        self.__cars_repository.create(car)
        self.__undo_service.add_to_undo(AddOperation(self.__cars_repository, car))

    def delete(self, id_car):
        car = self.__cars_repository.find_by_id(id_car)
        self.__cars_repository.delete(id_car)
        self.__undo_service.add_to_undo(DeleteOperation(self.__cars_repository, car))

    def update(self, id_car, model, purchase_year, km_travelled, in_warranty):
        car = self.__cars_repository.find_by_id(id_car)
        if car is None:
            raise KeyError(f"The car with id: {id_car} doesn't exist.")

        if model != '':
            car.model = model
        if purchase_year != '':
            car.purchase_year = purchase_year
        if km_travelled != '':
            car.km_travelled = km_travelled
        if in_warranty != '':
            car.in_warranty = in_warranty

        self.__car_validator.validate(car)

        if in_warranty == 'yes' or in_warranty == '':
            car.in_warranty = True
        else:
            car.in_warranty = False

        self.__cars_repository.update(car)

    def get_all(self):
        return self.__cars_repository.get_all()

    def merge_sort(self, arr, key=lambda x: x[1]):
        if len(arr) < 2:
            return arr
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        left = arr[:mid]
        # into 2 halves
        right = arr[mid:]

        # Sorting the first half
        self.merge_sort(left)
        # Sorting the second half
        self.merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if key(left[i]) > key(right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr

    def DObyWorkmanship(self):
        result = []
        for car in self.__cars_repository.get_all():
            sum_workmanship = 0
            for transaction in self.__transaction_repository.get_all():
                if car.id_entity == transaction.id_car:
                    sum_workmanship += transaction.sum_workmanship
            result.append((car.model, sum_workmanship))
        output = self.merge_sort(result, key=lambda tuple: tuple[1])
        return output

    def updateWarranty(self, current_year):
        output = []
        for car in self.__cars_repository.get_all():
            if current_year - car.purchase_year > 3 or car.km_travelled > 60000:
                output.append(car)
        return output

    def populate_cars(self, number_of_cars):

        in_warrantys = ['yes', 'no']
        models = ('toyota', 'audi', 'bmw', 'mercedes', 'ford', 'skoda', 'ferrari')
        for index in range(number_of_cars):
            id_car = random.randint(3, 1000000000000)
            model = random.choice(models)
            purchase_year = random.randint(1999, 2020)
            km_travelled = random.randint(200000, 500000)
            in_warranty = random.choice(in_warrantys)

            a_car = Car(id_car, model, purchase_year, km_travelled, in_warranty)
            self.__cars_repository.create(a_car)






