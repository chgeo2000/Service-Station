from Domain.Entity import Entity

import jsonpickle


class FileRepository:

    def __init__(self, filename):
        self.__storage = {}    # dictionary having as keys the ids of the entities and as values the entities themselves
        self.__filename = filename

    def __read_file(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__storage = jsonpickle.decode(f.read())
        except:
            self.__storage = {}

    def __write_file(self):
        with open(self.__filename, 'w') as f:
            f.write(jsonpickle.encode(self.__storage))

    def find_by_id(self, id_entity):

        self.__read_file()   # after I call read_file method in the dictionary-"storage" is what I have in the file.
        if str(id_entity) in self.__storage:
            return self.__storage[str(id_entity)]
        return None

    def create(self, entity: Entity):

        if self.find_by_id(entity.id_entity) is not None:
            raise KeyError(f'The entity with the id: {entity.id_entity} already exists.')

        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def update(self, entity: Entity):

        if self.find_by_id(entity.id_entity) is None:
            raise KeyError(f"We cannot update the entity with the id: {entity.id_entity} because it doesn't exist.")

        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def delete(self, id_entity):

        if self.find_by_id(id_entity) is None:
            raise KeyError(f"We cannot delete the entity with the id: {id_entity} because it doesn't exist.")

        del self.__storage[id_entity]
        self.__write_file()

    def get_all(self):

        self.__read_file()
        return list(self.__storage.values())
