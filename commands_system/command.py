from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def get_id(self: "Command") -> int:
        pass

    @abstractmethod
    def get_title(self: "Command") -> str:
        pass

    @abstractmethod
    def process(self: "Command", context: "CommandContext") -> None:
        pass
