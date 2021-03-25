from Domain.Entity import Entity


class CardClient(Entity):
    """
    It describes the "CardClient" entity.
    """

    def __init__(self, id_card, surname, firstname, cnp, birthdate, registration_date):
        super().__init__(id_card)
        self.__surname = surname
        self.__firstname = firstname
        self.__cnp = cnp
        self.__birthdate = birthdate
        self.__registration_date = registration_date

    # properties
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, new_firstname):
        self.__firstname = new_firstname

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        self.__cnp = new_cnp

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, new_birthdate):
        self.__birthdate = new_birthdate

    @property
    def registration_date(self):
        return self.__registration_date

    @registration_date.setter
    def registration_date(self, new_registration_date):
        self.__registration_date = new_registration_date

    def __str__(self):
        return f"id_card: {self.id_entity}, surname:{self.surname}, firstname:{self.firstname}, " \
               f"cnp: {self.cnp}, birthdate:{self.birthdate}, "\
               f"registration_date: {self.registration_date}"
