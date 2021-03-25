from Repository.FileRepository import FileRepository


class UndoOperation:
    def __init__(self, repository: FileRepository):
        self._repository = repository

    def undo(self):
        raise NotImplemented('A derived class must be used!')

