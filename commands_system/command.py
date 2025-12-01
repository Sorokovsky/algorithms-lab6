from abc import ABC, abstractmethod


class Command(ABC):
    _id: int

    def get_id(self: "Command") -> int:
        return self._id

    def set_id(self: "Command", new_id: int) -> None:
        self._id = new_id

    @abstractmethod
    def get_title(self: "Command") -> str:
        pass

    @abstractmethod
    def process(self: "Command", context: "CommandContext") -> None:
        pass
