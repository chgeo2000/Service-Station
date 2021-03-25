from Tests.TestDomain import *
from Tests.TestRepository import *
from Tests.TestCarService import *
from Tests.TestCardClientService import *
from Tests.TestTransactionService import *


def run_all():
    testCar()
    testCardClient()
    testTransaction()
    testCreateRepository()
    testDeleteRepository()
    testUpdateRepository()
    testGetAllRepository()
    testMergeSort()
    testDOByWorkmanship()
    testPopulateCars()
    testDOByDiscount()
    testGetTransactionsInInterval()

