import datetime
from Domain.Transaction import Transaction


class TransactionValidator:

    def validate(self, transaction: Transaction):
        """
        It validates the "transaction" entity.
        """
        error_list = []

        date = transaction.date
        year, month, day = date.split('.')

        is_valid_date = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            is_valid_date = False

        if not is_valid_date:
            error_list.append("The date format you chose is incorrect. Try again.")

        hour = transaction.hour
        hour, minute, second = hour.split(':')

        is_valid_hour = True
        try:
            datetime.time(int(hour), int(minute), int(second))
        except ValueError:
            is_valid_hour = False

        if not is_valid_hour:
            error_list.append("The hour format you chose is incorrect. Try again.")

        if error_list:
            raise ValueError(error_list)
