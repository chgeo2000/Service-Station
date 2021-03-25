from Domain.UndoOperation import UndoOperation
from Repository.FileRepository import FileRepository


class AddOperation(UndoOperation):
    def __init__(self, repository: FileRepository, added_object):
        super().__init__(repository)
        self.__added_object = added_object

    def undo(self):
        self._repository.delete(self.__added_object.id_entity)


