from xlwt import Workbook
from Repository.FileRepository import FileRepository


class ExcelExportService:
    def __init__(self, car_repository: FileRepository):
        self.__car_repository = car_repository

    def export(self):
        workbook = Workbook()
        sheet1 = workbook.add_sheet("Sheet 1")
        for i in range(0, len(self.__car_repository.get_all())):
            sheet1.write(i, 0, str(self.__car_repository.get_all()[i]))
        workbook.save("xlwt example.xls")
