import datetime
from Domain.CardClient import CardClient


class CardClientValidator:

    def validate(self, card_client: CardClient):
        """
            It validates the "cardclient" entity.
        """
        error_list = []

        birthdate = card_client.birthdate
        day, month, year = birthdate.split('.')

        is_valid_birthdate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            is_valid_birthdate = False

        if not is_valid_birthdate:
            error_list.append("The birthdate format you chose is incorrect. Try again.")

        registration_date = card_client.registration_date
        day, month, year = registration_date.split('.')

        is_valid_registration_date = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            is_valid_registration_date = False

        if not is_valid_registration_date:
            error_list.append("The registration date format you chose is incorrect. Try again.")

        if len(error_list) != 0:
            raise ValueError(error_list)
