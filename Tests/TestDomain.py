from Domain.Car import Car
from Domain.CardClient import CardClient
from Domain.Transaction import Transaction


def testCar():
    car = Car("1", "ford", 1990, 200000, "no")
    assert car.id_entity == "1"
    assert car.model == "ford"
    assert car.purchase_year == 1990
    assert car.km_travelled == 200000
    assert car.in_warranty == "no"


def testCardClient():
    card_client = CardClient("1", "Chira", "George", 50011137777, "13.11.2000", "13.11.2014")
    assert card_client.id_entity == "1"
    assert card_client.surname == "Chira"
    assert card_client.firstname == "George"
    assert card_client.cnp == 50011137777
    assert card_client.birthdate == "13.11.2000"
    assert card_client.registration_date == "13.11.2014"


def testTransaction():
    transaction = Transaction("1", "1", "1", 100, 30, "2000.03.26", "15:28:00")
    assert transaction.id_entity == "1"
    assert transaction.id_car == "1"
    assert transaction.id_card == "1"
    assert transaction.sum_pieces == 100
    assert transaction.sum_workmanship == 30
    assert transaction.date == "2000.03.26"
    assert transaction.hour == "15:28:00"
