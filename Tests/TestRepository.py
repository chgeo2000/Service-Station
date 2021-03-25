from Domain.Entity import Entity
from Domain.Car import Car
from Repository.FileRepository import FileRepository
from Tests.Utils import clear_file


# All the tests I've made are self explanatory


def testCreateRepository():
    """
    Tests for create method
    """
    clear_file("repository_test.txt")
    entities_repository = FileRepository("repository_test.txt")

    entity1 = Entity('1')

    entities_repository.create(entity1)
    assert len(entities_repository.get_all()) == 1
    added = entities_repository.find_by_id('1')
    assert added is not None
    assert added.id_entity == '1'

    try:
        entity2 = Entity('1')
        entities_repository.create(entity2)
        assert False  # id must be unique

    except Exception:
        assert True


def testDeleteRepository():
    """
    Tests for delete method.
    """
    clear_file("repository_test.txt")
    entities_repository = FileRepository("repository_test.txt")

    try:
        entities_repository.delete("1")  # we cannot delete an entity if that entity doesn't even exist
        assert False

    except Exception:
        assert True

    entity1 = Entity('1')
    entities_repository.create(entity1)
    assert len(entities_repository.get_all()) == 1

    entities_repository.delete("1")
    assert len(entities_repository.get_all()) == 0


def testUpdateRepository():
    """
    Tests for update method"
    """

    clear_file("repository_test.txt")
    cars_repository = FileRepository("repository_test.txt")

    car = Car("1", "ford", 1990, 200000, "no")
    cars_repository.create(car)

    assert len(cars_repository.get_all()) == 1

    cars_repository.update(car)
    assert car.model == "ford"   #because at repository-level there's no difference between create and update


def testGetAllRepository():
    """
    Tests for get all method
    """
    clear_file("repository_test.txt")
    entities_repository = FileRepository("repository_test.txt")

    entity1 = Entity('1')

    entities_repository.create(entity1)
    assert len(entities_repository.get_all()) == 1
    assert entities_repository.get_all() == [entity1]
