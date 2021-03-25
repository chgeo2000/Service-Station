from Domain.UndoOperation import UndoOperation


class UndoService:
    def __init__(self):
        self.__undo_stack = []

    def add_to_undo(self, operation: UndoOperation):
        self.__undo_stack.append(operation)

    def do_undo(self):
        if len(self.__undo_stack) > 0:
            self.__undo_stack.pop().undo()
