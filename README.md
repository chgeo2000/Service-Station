# Service-Station
 Python application using OOP and Stratified Architecture. Designed for managing a service station, supporting cars, clientcards and transactions.
 ##### Service station application having the following functionalities:
  1. CRUD operations for:
     - Cars
       - id_car, model, purchase_year, km_travelled, in_warranty
     - Clientcard
       - id_card, surname, firstname, cnp, birthdate, registration_date
     - Transactions
       - id_transaction, id_car, id_card, sum_pieces, sum_workmanship, date, hour 
  2. Saving and reading objects to/from .txt files using jsonpickle library.
  3. Listing implemented for all domain objects, with extended functionalities:
     - Listing all transactions with the sum within a given range (sum  = sum_pieces + sum_workmanship), using both, a simple "for loop" and the "filter" method.
     - Listing all cars in descending order (using merge sort) by the sum obtained per workmanship.
     - Listing all clientcards in descending order (using python's built in "sorted") by the value of the discounts obtained.
  4. Searching cars and clients after model, purchase year, km travelled, surname, firstname and cnp. Full text - search. 
  5. Removal of all transactions within a certain number of days.
  6. Warranty update for each car.
  7. Populate "car entity" with custom number of objects.
  8. 
