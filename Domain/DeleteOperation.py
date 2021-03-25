from Domain.UndoOperation import UndoOperation
from Repository.FileRepository import FileRepository


class DeleteOperation(UndoOperation):
    def __init__(self, repository: FileRepository, deleted_object):
        super().__init__(repository)
        self.__deleted_object = deleted_object

    def undo(self):
        self._repository.create(self.__deleted_object)

