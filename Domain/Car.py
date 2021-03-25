from Domain.Entity import Entity


class Car(Entity):
    """
       It describes the "Car" entity.
    """

    def __init__(self, id_car, model, purchase_year, km_travelled, in_warranty):

        super().__init__(id_car)
        self.__model = model
        self.__purchase_year = purchase_year
        self.__km_travelled = km_travelled
        self.__in_warranty = in_warranty

    # properties
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def purchase_year(self):
        return self.__purchase_year

    @purchase_year.setter
    def purchase_year(self, new_purchase_year):
        self.__purchase_year = new_purchase_year

    @property
    def km_travelled(self):
        return self.__km_travelled

    @km_travelled.setter
    def km_travelled(self, new_km_travelled):
        self.__km_travelled = new_km_travelled

    @property
    def in_warranty(self):
        return self.__in_warranty

    @in_warranty.setter
    def in_warranty(self, new_in_warranty):
        self.__in_warranty = new_in_warranty

    def __str__(self):
        return f"id_car: {self.id_entity}, model: {self.model}, purchase_year: {self.purchase_year}, "\
               f"km_travelled: {self.km_travelled}, in_warranty: {self.in_warranty} "
