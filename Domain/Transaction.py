from Domain.Entity import Entity


class Transaction(Entity):
    """
    It describes the "Transaction" entity.
    """

    def __init__(self, id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour):
        super().__init__(id_transaction)
        self.__id_car = id_car
        self.__id_card = id_card
        self.__sum_pieces = sum_pieces
        self.__sum_workmanship = sum_workmanship
        self.__date = date
        self.__hour = hour

    # properties
    @property
    def id_car(self):
        return self.__id_car

    @id_car.setter
    def id_car(self, new_id_car):
        self.__id_car = new_id_car

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, new_id_card):
        self.__id_card = new_id_card

    @property
    def sum_pieces(self):
        return self.__sum_pieces

    @sum_pieces.setter
    def sum_pieces(self, new_sum_pieces):
        self.__sum_pieces = new_sum_pieces

    @property
    def sum_workmanship(self):
        return self.__sum_workmanship

    @sum_workmanship.setter
    def sum_workmanship(self, new_sum_workmanship):
        self.__sum_workmanship = new_sum_workmanship

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, new_hour):
        self.__hour = new_hour

    def __str__(self):
        return f"id_transaction: {self.id_entity}, id_car:{self.id_car}, "\
               f"id_card: {self.id_card}, sum_pieces: {self.sum_pieces}, "\
               f"sum_workmanship: {self.sum_workmanship}, date: {self.date}, "\
               f"hour: {self.hour}"
