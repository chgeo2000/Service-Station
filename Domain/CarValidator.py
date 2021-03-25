from Domain.Car import Car


class CarValidator:

    def validate(self, car: Car):

        """
        It validates the "car" entity.
        """

        error_list = []
        if car.km_travelled < 0:
            error_list.append('Number of kilometers must be a positive number.')

        if car.purchase_year < 0:
            error_list.append("Purchase year must be a positive number.")

        if car.in_warranty not in ["yes", "no"]:
            error_list.append("A car can only be in warranty or not. ")

        if error_list:
            raise ValueError(error_list)
