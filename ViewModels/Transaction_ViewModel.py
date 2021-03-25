from Domain.Car import Car
from Domain.CardClient import CardClient


class TransactionViewModel:

    def __init__(self, id_transaction, car: Car, card_client: CardClient, sum_pieces, sum_workmanship, date, hour):
        self.id_transaction = id_transaction
        self.car = car
        self.card_client = card_client
        self.sum_pieces = sum_pieces
        self.sum_workmanship = sum_workmanship
        self.date = date
        self.hour = hour

    def __str__(self):
        return f'Id transaction: {self.id_transaction} \n-------with the Car: {self.car} \n-------and Card client {self.card_client} \n -------sum pieces: {self.sum_pieces}, sum_workmanship {self.sum_workmanship}, date: {self.date}, hour: {self.hour}'

